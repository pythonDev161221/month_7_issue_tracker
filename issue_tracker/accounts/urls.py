from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

# from accounts.views import login_view, logout_view
from accounts.views import RegisterView, UserProfileView, UserChangeUpdateView, UserPasswordChangeView

app_name = "accounts"

urlpatterns = [
    # path('login/', login_view, name='login_view'),
    # path('logout/', logout_view, name='logout_view'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change/', UserChangeUpdateView.as_view(),
         name='user_change_update_view'),
    path('profile/<int:pk>/password_change', UserPasswordChangeView.as_view(),
         name='user_password_change_view'),
]
