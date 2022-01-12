from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import IssueForm
from webapp.models import Issue, Status, Type


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
        return super().get_context_data(**kwargs)

# class AddIssueView(View):
#
#     def get(self):
#         return render(self.request, 'issue_view.html')

def AddView(request):
    if request.method == 'GET':
        form = IssueForm()
        context = {'form': form}
        return render(request, "add_issue_view.html", context)
    else:
        form = IssueForm(data=request.POST)
        if form.is_valid():
            summary = request.POST.get('summary')
            description = request.POST.get('description')
            status_pk = request.POST.get('status')
            type_pk = request.POST.get('type')
            status = Status.objects.get(pk=status_pk)
            type = Type.objects.get(pk=type_pk)

            new_issue = Issue(summary=summary, description=description,
                          status=status, type=type)
            new_issue.save()
    return redirect('index_view')
