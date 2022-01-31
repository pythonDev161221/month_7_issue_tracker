from django.urls import path
from .views import IndexView, IssueView, IssueDeleteView, CreateIssueView, IssueUpdateView
from .views.projects import ProjectListView, ProjectCreateView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list_view'),
    path('project/create', ProjectCreateView.as_view(), name='project_create_view'),
    path('project/<int:project_pk>', ProjectDetailView.as_view(), name='project_detail_view'),
    path('project/<int:project_pk>/issue/create', CreateIssueView.as_view(), name='create_issue_view'),
    path('project/<int:project_pk>/issue/<int:pk>/update', IssueUpdateView.as_view(), name='issue_update_view'),

    path('issue/<int:project_pk>/', IndexView.as_view(), name='index_view'),
    path('project/<int:project_pk>/issue/<int:issue_pk>/detail/', IssueView.as_view(),
         name='issue_view'),
    # path('issue/add/', AddIssueView.as_view(), name='add_issue_view'),
    # path('issue/<int:issue_pk>/update/', IssueUpdateView.as_view(),
    #      name='update_issue_view'),
    path('project/<int:project_pk>/issue/<int:issue_pk>/delete', IssueDeleteView.as_view(),
         name='issue_delete_view'),
    # path('issue/search/', SearchView.as_view(), name='search_view')
]
