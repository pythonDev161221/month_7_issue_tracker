from django.urls import path
from webapp.views import ProjectListView

app_name = "accounts"

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list_view'),
]