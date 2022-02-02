
from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView

from webapp.forms import IssueForm
from webapp.models import Issue, Project


class CreateIssueView(CreateView):
    model = Issue
    template_name = 'issues/create_issue_view.html'
    form_class = IssueForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        issue = form.save(commit=False)
        issue.project = project
        issue.save()
        return super(CreateIssueView, self).form_valid(form)

    def get_success_url(self):
        return reverse('project_detail_view', kwargs={'project_pk': self.kwargs.get('project_pk')})


class IssueUpdateView(UpdateView):
    model = Issue
    template_name = 'issues/issue_update_view.html'
    form_class = IssueForm
    pk_url_kwarg = 'issue_pk'

    def get_success_url(self):
        return reverse('project_detail_view', kwargs={'project_pk': self.kwargs.get('project_pk')})


# class IssueDeleteView(View):
#     def get(self, request, *args, **kwargs):
#         issue = get_object_or_404(Issue, pk=kwargs.get('issue_pk'))
#         project_pk = kwargs.get('project_pk')
#         return render(request, 'issues/issue_delete.html', {'issue': issue, 'project_pk': project_pk})
#
#     def post(self, request, *args, **kwargs):
#         issue = get_object_or_404(Issue, pk=kwargs.get('issue_pk'))
#         issue.delete()
#         return redirect('project_list_view')

class IssueDeleteView(DeleteView):
    template_name = 'issues/issue_delete.html'
    model = Issue
    pk_url_kwarg = 'issue_pk'

    def get_success_url(self):
        return reverse('project_list_view')


class IssueDetailView(DetailView):
    template_name = 'issues/issue_detail_view.html'
    model = Issue
    pk_url_kwarg = 'issue_pk'
    context_object_name = 'issue'


class IssueListView(ListView):
    template_name = 'issues/issue_list_view.html'
    model = Issue







