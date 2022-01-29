from django.views.generic import ListView

from webapp.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list_view.html'
    context_object_name = 'projects'
