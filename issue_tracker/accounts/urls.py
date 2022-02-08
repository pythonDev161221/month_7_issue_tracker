from django.urls import path

from accounts.views import login_view, logout_view
from webapp.views import ProjectListView

app_name = "accounts"

urlpatterns = [
    path('', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
]
