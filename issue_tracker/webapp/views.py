from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView, ListView

from webapp.forms import IssueForm, SearchForm
from .models import Issue, Status, Type
from webapp.base import FormView as CustomFormView


# class IndexView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         issues = Issue.objects.all()
#         kwargs['issues'] = issues
#         form = SearchForm()
#         kwargs['form'] = form
#         if self.request.GET.get('search'):
#             issues = Issue.objects.filter(summary__icontains=self.request.GET.get('search'))
#             kwargs['issues'] = issues
#         return kwargs

class IndexView(ListView):
    template_name = 'index.html'
    model = Issue
    context_object_name = 'issues'
    paginate_by = 10
    paginate_orphans = 2

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('search'):
            query = Q(summary__icontains=self.request.GET.get('search')) | \
                    Q(description__icontains=self.request.GET.get('search'))
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs = super().get_context_data(object_list=object_list, **kwargs)
        kwargs['form'] = SearchForm()
        if self.search_value:
            kwargs['search'] = self.search_value
        return kwargs

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')


class IssueView(TemplateView):
    template_name = 'issue_view.html'

    def get_context_data(self, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('issue_pk'))
        kwargs['issue'] = issue
        return super().get_context_data(**kwargs)


# class AddIssueView(View):

#
#     def get(self, request, *args, **kwargs):
#         form = IssueForm()
#         context = {'form': form}
#         return render(request, "add_issue_view.html", context)
#
#     def post(self, request, *args, **kwargs):
#         form = IssueForm(data=request.POST)
#         if form.is_valid():
#             type_names = form.cleaned_data.pop('type_names')
#
#             summary = request.POST.get('summary')
#             description = request.POST.get('description')
#             status_pk = request.POST.get('status')
#             status = Status.objects.get(pk=status_pk)
#             # new_issue = Issue.objects.create(**form.cleaned_data)
#
#             new_issue = Issue.objects.create(summary=summary, description=description,
#                                  status=status)
#             new_issue.type_names.set(type_names)
#             return redirect('issue_view', issue_pk=new_issue.pk)
#         return render(request, "add_issue_view.html", {'form': form})

class AddIssueView(CustomFormView):
    template_name = 'add_issue_view.html'
    form_class = IssueForm

    def form_valid(self, form):
        data = {}
        type_names = form.cleaned_data.pop('type_names')
        for key, value in form.cleaned_data.items():
            if value is not None:
                data[key] = value
        self.issue = Issue.objects.create(**data)
        self.issue.type_names.set(type_names)
        return super().form_valid(form)

    def get_redirect_url(self):
        return reverse('issue_view', kwargs={'issue_pk': self.issue.pk})


# class UpdateIssueView(CustomFormView):
#     template_name = 'update_issue_view.html'
#     form_class = IssueForm
#
#     def dispatch(self, request, *args, **kwargs):
#         self.issue = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_object(self):
#         pk = self.kwargs.get('issue_pk')
#         return get_object_or_404(Issue, pk=pk)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['issue'] = self.issue
#         return context
#
#     # def get_initial(self):
#     #     initial = {}
#     #     for key in 'summary', 'description', 'status':
#     #         initial[key] = getattr(self.issue, key)
#     #     initial['type_names'] = self.issue.type_names.all()
#     #     return initial
#
#
#     def form_valid(self, form):
#         # type_names = form.cleaned_data.pop('type_names')
#         # for key, value in form.cleaned_data.items():
#         #     if value is not None:
#         #         setattr(self.issue, key, value)
#         # self.issue.save()
#         # self.issue.type_names.set(type_names)
#         self.issue = form.save()
#
#         return super().form_valid(form)
#
#     def get_redirect_url(self):
#         return reverse('issue_view', kwargs={'issue_pk': self.issue.pk})


class UpdateIssueView(FormView):
    form_class = IssueForm
    template_name = 'update_issue_view.html'

    def dispatch(self, request, *args, **kwargs):
        self.issue = self.get_object()
        # return super().dispatch(request, *args, **kwargs)
        return super(UpdateIssueView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Issue, pk=self.kwargs.get('issue_pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = self.issue
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.issue
        return kwargs

    def form_valid(self, form):
        self.issue = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issue_view', kwargs={'issue_pk': self.issue.pk})


class IssueDeleteView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('issue_pk'))
        return render(request, 'issue_delete.html', {'issue': issue})

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('issue_pk'))
        issue.delete()
        return redirect('index_view')
