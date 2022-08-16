from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login, login
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.generic import ListView, DetailView

from accounts.forms import MyUserCreationForm
from accounts.models import Profile


class LoginView(LoginView):
    template_name = "registration/login.html"
    post_redirect = None


    def get(self, request, *args, **kwargs):
        self.object = None
        post_redirect = request.META.get('HTTP_REFERER')
        print(self.object,post_redirect)
        return super().get(request, *args, **kwargs)
#
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.post_redirect)
#
#
#     def post(self, request, *args, **kwargs):
#         """Logout may be done via POST."""
#         self.object, self.redirect_url = self.get( request, *args, **kwargs)
#         print(self.redirect_url)
#         return self.object, self.redirect_url
#     #
#     #
#     # def get_redirect_url(self):
#     #     """Return the user-originating redirect URL if it's safe."""
#     #     x,redirect_url = self.post()
#     #     print(self.request)
#     #     redirect_to = redirect_url
#     #     print(redirect_to)
#     #     url_is_safe = url_has_allowed_host_and_scheme(
#     #         url=redirect_to,
#     #         allowed_hosts=self.get_success_url_allowed_hosts(),
#     #         require_https=self.request.is_secure(),
#     #     )
#     #     return HttpResponseRedirect(self.request.META.get('HTTP_REFERER')) if url_is_safe else ""
#     if post:
#         def get_success_url(self):
#             x, redirect_url = self.post()
#             print(self.request)
#             redirect_to = redirect_url
#             print(self.request.META.get('HTTP_REFERER','/'))
#             return HttpResponseRedirect(redirect_to)
#

def register_view(request, *args, **kwargs):

    if request.method == 'POST':
        try:
            form = MyUserCreationForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('webapp:IndexView')
        except: ValidationError
    else:
        form = MyUserCreationForm()
    return render(request, 'user_create.html', context={'form': form})

class UsersView(PermissionRequiredMixin,ListView):
    template_name = 'usersall.html'
    model = Profile
    context_object_name = 'user'

class UserDetailView(PermissionRequiredMixin,DetailView):
    template_name = 'user.html'
    model = Profile
    context_object_name = 'user'


