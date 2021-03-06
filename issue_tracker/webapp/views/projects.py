from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import ProjectForm, ProjectUserForm
from webapp.models import Project, Issue


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list_view.html'
    context_object_name = 'projects'
    paginate_by = 10
    paginate_orphans = 1


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create_view.html'
    permission_required = 'webapp.add_project'

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()
        self.object.users.add(self.request.user)
        return HttpResponseRedirect(self.get_success_url())

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


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_delete_view.html'
    pk_url_kwarg = 'project_pk'
    permission_required = 'webapp.delete_project'

    def get_success_url(self):
        return reverse('webapp:project_list_view')


class ProjectUserListView(PermissionRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_user_list_view.html'
    pk_url_kwarg = 'project_pk'
    permission_required = 'webapp.can_manage_users'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()

    def get_success_url(self):
        return reverse('webapp:project_list_view')


class ProjectUserAddView(PermissionRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectUserForm
    pk_url_kwarg = 'project_pk'
    template_name = 'projects/project_user_add_view.html'
    permission_required = 'webapp.can_manage_users'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()

    def get_success_url(self):
        return reverse('webapp:project_user_list_view',
                       kwargs={'project_pk': self.kwargs.get('project_pk')})
