from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from accounts.forms import MyUserCreateForm


class RegisterView(CreateView):
    model = User
    template_name = "registration.html"
    form_class = MyUserCreateForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse("webapp:project_list_view")
        return next_url


class UserProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "profile.html"
    context_object_name = "user_object"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        projects_join = self.object.projects_join.all()
        kwargs['projects'] = projects_join
        return kwargs



# Create your views here.
# def login_view(request):
#     context = {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('webapp:project_list_view')
#         else:
#             context['has_error'] = True
#     return render(request, 'registration/login.html', context=context)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('webapp:project_list_view')
