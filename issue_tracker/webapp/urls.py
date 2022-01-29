from django.urls import path
from .views import IndexView, IssueView, AddIssueView, UpdateIssueView, IssueDeleteView
from .views.projects import ProjectListView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list_view'),
    path('issue/<int:project_pk>/', IndexView.as_view(), name='index_view'),
    path('issue/<int:issue_pk>/detail/', IssueView.as_view(), name='issue_view'),
    path('issue/add/', AddIssueView.as_view(), name='add_issue_view'),
    path('issue/<int:issue_pk>/update/', UpdateIssueView.as_view(), name='update_issue_view'),
    path('issue/<int:issue_pk>/delete', IssueDeleteView.as_view(), name='issue_delete_view'),
    # path('issue/search/', SearchView.as_view(), name='search_view')
]
