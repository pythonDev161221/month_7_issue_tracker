from django.urls import path
from .views import IssueDeleteView, CreateIssueView, IssueUpdateView, IssueDetailView, IssueListView
from .views.projects import ProjectListView, ProjectCreateView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView, \
    ProjectUserListView, ProjectUserAddView

app_name = 'webapp'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list_view'),
    path('project/create', ProjectCreateView.as_view(), name='project_create_view'),
    path('project/<int:project_pk>', ProjectDetailView.as_view(), name='project_detail_view'),
    path('project/<int:project_pk>/issue/create', CreateIssueView.as_view(), name='create_issue_view'),
    path('project/<int:project_pk>/update/', ProjectUpdateView.as_view(), name='project_update_view'),
    path('project/<int:project_pk>/delete/', ProjectDeleteView.as_view(), name='project_delete_view'),

    path('project/<int:project_pk>/issue/<int:issue_pk>/update', IssueUpdateView.as_view(),
         name='issue_update_view'),
    path('project/<int:project_pk>/issue/<int:issue_pk>/delete', IssueDeleteView.as_view(),
         name='issue_delete_view'),
    path('project/issue/<int:issue_pk>/detail/', IssueDetailView.as_view(),
         name='issue_detail_view'),
    path('issue', IssueListView.as_view(), name='issue_list_view'),
    path('project/<int:project_pk>/users/', ProjectUserListView.as_view(),
         name='project_user_list_view'),
    path('project/<int:project_pk>/users/add/', ProjectUserAddView.as_view(),
         name='project_user_add_view'),
]
