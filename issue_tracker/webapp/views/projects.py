from django.core.exceptions import ImproperlyConfigured
from django.db.models import F
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

    # def get_queryset(self):
    #     queryset_all = super(ProjectDetailView, self).get_queryset()
    #     print(queryset_all)
    #     return queryset_all

    # def get_object(self, queryset=None):
    #     obj = super().get_object()
    #     print(obj)
    #     obj.issues.filter(is_deleted__exact=False)
    #     obj = obj - obj.issues.filter(is_deleted__exact=False)
    #     q1 = obj.issues.filter(is_deleted__exact=True)
    #     q2 = obj.issues.all()
    #     obj.issues.set(obj.issues.filter(is_deleted__exact=True))
    #     obj.save()
    #
    #     print(obj.issues.all().exclude(is_deleted__exact=True))
    #     print(obj.issues.filter(is_deleted__exact=True))
    #     return obj

    # def get_queryset(self):
    #     """
    #     Return the `QuerySet` that will be used to look up the object.
    #
    #     This method is called by the default implementation of get_object() and
    #     may not be called if get_object() is overridden.
    #     """
    #     if self.queryset is None:
    #         if self.model:
    #             return self.model._default_manager.all()
    #         else:
    #             raise ImproperlyConfigured(
    #                 "%(cls)s is missing a QuerySet. Define "
    #                 "%(cls)s.model, %(cls)s.queryset, or override "
    #                 "%(cls)s.get_queryset()." % {
    #                     'cls': self.__class__.__name__
    #                 }
    #             )
    #     return self.queryset.all()
    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context['object'] = self.object
            print('object')
            print(self.object.pk)
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
            issues = Issue.objects.filter(project__exact=self.object.pk, is_deleted__exact=False)
            context['issues'] = issues
        context.update(kwargs)
        return super().get_context_data(**context)


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
