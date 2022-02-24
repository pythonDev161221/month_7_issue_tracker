from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView

from webapp.forms import IssueForm
from webapp.models import Issue, Project


class CreateIssueView(PermissionRequiredMixin, CreateView):
    model = Issue
    template_name = 'issues/create_issue_view.html'
    form_class = IssueForm
    permission_required = 'webapp.add_issue'

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        return super().has_permission() and self.request.user in project.users.all()

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        issue = form.save(commit=False)
        issue.project = project
        issue.author = self.request.user
        issue.save()
        return super(CreateIssueView, self).form_valid(form)

    def get_success_url(self):
        return reverse('webapp:project_detail_view', kwargs={'project_pk': self.kwargs.get('project_pk')})


class IssueUpdateView(PermissionRequiredMixin, UpdateView):
    model = Issue
    template_name = 'issues/issue_update_view.html'
    form_class = IssueForm
    pk_url_kwarg = 'issue_pk'
    permission_required = 'webapp.change_issue'

    def has_permission(self):
        return super().has_permission() and \
               any(user == self.request.user for user in self.get_object().project.users.all())

    def get_success_url(self):
        return reverse('webapp:project_detail_view',
                       kwargs={'project_pk': self.kwargs.get('project_pk')})


class IssueDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'issues/issue_delete.html'
    model = Issue
    pk_url_kwarg = 'issue_pk'
    permission_required = 'webapp.delete_issue'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.users.all()

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse('webapp:project_list_view')


class IssueDetailView(DetailView):
    template_name = 'issues/issue_detail_view.html'
    model = Issue
    pk_url_kwarg = 'issue_pk'
    context_object_name = 'issue'


class IssueListView(ListView):
    template_name = 'issues/issue_list_view.html'
    model = Issue
    context_object_name = 'issues'
    paginate_by = 12
    paginate_orphans = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_deleted__exact=False)
        return queryset
