from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView

from webapp.models import Issue


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        issues = Issue.objects.all()
        kwargs['issues'] = issues
        return kwargs


class IssueView(TemplateView):
    template_name = 'issue_view.html'

    def get_context_data(self, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['issue_pk'])
        kwargs['issue'] = issue
        return kwargs
