from django.urls import reverse
from django.views.generic import ListView, CreateView

from webapp.forms import ProjectForm
from webapp.models import Project


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
