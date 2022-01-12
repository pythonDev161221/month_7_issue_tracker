from django.urls import path
from .views import IndexView, IssueView

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
    path('detail/<int:issue_pk>', IssueView.as_view(), name='issue_view')

]
