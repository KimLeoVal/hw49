from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import request
from django.utils.http import url_has_allowed_host_and_scheme


# class LoginView(LoginView):
#     template_name = "registration/login.html"
#
#     def get_success_url(self):
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


