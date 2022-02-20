from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.db.models import F
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import ProjectForm, ProjectUserForm
from webapp.models import Project, Issue


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list_view.html'
    context_object_name = 'projects'
    paginate_by = 5
    paginate_orphans = 1


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create_view.html'

    permission_required = 'webapp.add_project'

    def has_permission(self):
        return super().has_permission()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:project_list_view')


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project_detail_view.html'
    pk_url_kwarg = 'project_pk'

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            issues = Issue.objects.filter(project__exact=self.object.pk, is_deleted__exact=False)
            context['issues'] = issues
        context.update(kwargs)
        return super().get_context_data(**context)


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/project_update_view.html'
    pk_url_kwarg = 'project_pk'
    form_class = ProjectForm
    permission_required = 'webapp.change_project'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_delete_view.html'
    pk_url_kwarg = 'project_pk'
    permission_required = 'webapp.delete_project'

    def has_permission(self):
        return super().has_permission()

    def get_success_url(self):
        return reverse('webapp:project_list_view')


class ProjectUserListView(PermissionRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_user_list_view.html'
    pk_url_kwarg = 'project_pk'
    permission_required = 'webapp.can_manage_users'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('webapp:project_list_view')


class ProjectUserAddView(PermissionRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectUserForm
    pk_url_kwarg = 'project_pk'
    template_name = 'projects/project_user_add_view.html'
    permission_required = 'webapp.change_project'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user



    def get_success_url(self):
        return reverse('webapp:project_user_list_view',
                       kwargs={'project_pk': self.kwargs.get('project_pk')})
