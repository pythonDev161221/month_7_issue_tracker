from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import ProjectForm
from webapp.models import Project, Issue


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list_view.html'
    context_object_name = 'projects'
    paginate_by = 3


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create_view.html'

    def get_success_url(self):
        return reverse('project_list_view')


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project_detail_view.html'
    pk_url_kwarg = 'project_pk'


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_update_view.html'
    pk_url_kwarg = 'project_pk'
    form_class = ProjectForm


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_delete_view.html'
    pk_url_kwarg = 'project_pk'

    def get_success_url(self):
        return reverse('project_list_view')
