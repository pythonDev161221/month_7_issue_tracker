from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView

from webapp.forms import IssueForm, SearchForm
from webapp.models import Issue, Status, Type
from webapp.base import FormView as CustomFormView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        issues = Issue.objects.all()
        kwargs['issues'] = issues
        form = SearchForm()
        kwargs['form'] = form
        if self.request.GET.get('search'):
            issues = Issue.objects.filter(summary=self.request.GET.get('search'))
            kwargs['issues'] = issues
        return kwargs


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


# class UpdateIssueView(View):
#     def get(self, request, *args, **kwargs):
#         issue = get_object_or_404(Issue, pk=kwargs.get('issue_pk'))
#         form = IssueForm(initial={
#             'summary': issue.summary,
#             'description': issue.description,
#             'status': issue.status,
#             'type_names': issue.type_names.all(),
#         })
#         context = {'form': form, 'issue': issue}
#         return render(request, "update_issue_view.html", context)
#
#     def post(self, request, *args, **kwargs):
#         form = IssueForm(data=request.POST)
#         issue = get_object_or_404(Issue, pk=kwargs.get('issue_pk'))
#         if form.is_valid():
#             type_names = form.cleaned_data.pop('type_names')
#             issue.summary = request.POST.get('summary')
#             issue.description = request.POST.get('description')
#             status_pk = request.POST.get('status')
#             # type_pk = request.POST.get('type')
#             issue.status = Status.objects.get(pk=status_pk)
#             # issue.type_names = Type.objects.get(pk=type_pk)
#             issue.type_names.set(type_names)
#             issue.save()
#
#             return redirect('issue_view', issue_pk=issue.pk)
#         return render(request, "update_issue_view.html", {'form': form, 'issue': issue})

class UpdateIssueView(FormView):
    template_name = 'update_issue_view.html'
    form_class = IssueForm
    redirect_url = ''

    def dispatch(self, request, *args, **kwargs):
        print('dispatch')
        self.issue = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        print('get_object')
        pk = self.kwargs.get('issue_pk')
        return get_object_or_404(Issue, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = self.issue
        return context

    def get_initial(self):
        initial = {}
        for key in 'summary', 'description', 'status':
            initial[key] = getattr(self.issue, key)
        initial['type_names'] = self.issue.type_names.all()
        return initial

    def form_valid(self, form):
        print('form_valid_start')
        type_names = form.cleaned_data.pop('type_names')
        for key, value in form.cleaned_data.items():
            if value is not None:
                setattr(self.issue, key, value)
        self.issue.save()
        self.issue.type_names.set(type_names)
        print('form_valid_end')
        return super().form_valid(form)

    def get_success_url(self):
        print('get_success_url')
        return reverse('issue_view', kwargs={'issue_pk': self.issue.pk})


class IssueDeleteView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('issue_pk'))
        return render(request, 'issue_delete.html', {'issue': issue})

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('issue_pk'))
        issue.delete()
        return redirect('index_view')
