from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

from webapp.forms import ProjectForm, ProjectIssueCreateForm
from webapp.models import Project, Issue


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list_view.html'
    context_object_name = 'projects'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    # fields = ['start_date', 'finish_date', 'name', 'description']
    template_name = 'projects/project_create_view.html'

    def get_success_url(self):
        return reverse('project_list_view')


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project_detail_view.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ProjectDetailView, self).get_context_data(**kwargs)
    #     return context


class CreateIssueView(CreateView):
    model = Issue
    template_name = 'projects/create_issue_view.html'
    form_class = ProjectIssueCreateForm

    def form_valid(self, form):
        print('valid')
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        issue = form.save(commit=False)
        issue.project = project
        issue.save()
        return super(CreateIssueView, self).form_valid(form)

    # def form_invalid(self, form):
    #     print('invalid')
    #     return super(CreateIssueView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('project_list_view')



