from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import request
from django.utils.http import url_has_allowed_host_and_scheme


class LoginView(LoginView):
    template_name = "registration/login.html"



    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            print(request.GET)
            redirect_to = self.get()
            print(redirect_to)
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = None
        redirect_url = request.META.get('HTTP_REFERER')
        return super().post(request, *args, **kwargs),redirect_url
    # def get_redirect_url(self):
    #     """Return the user-originating redirect URL if it's safe."""
    #     print(self.request)
    #     redirect_to = request.META.get('HTTP_REFERER','/')
    #     print(redirect_to)
    #     url_is_safe = url_has_allowed_host_and_scheme(
    #         url=redirect_to,
    #         allowed_hosts=self.get_success_url_allowed_hosts(),
    #         require_https=self.request.is_secure(),
    #     )
    #     return HttpResponseRedirect(self.request.META.get('HTTP_REFERER')) if url_is_safe else ""
    #
    # def get_success_url(self):
    #     print(self.request.META.get('HTTP_REFERER','/'))
    #     return HttpResponseRedirect(self.request.META.get('HTTP_REFERER','/'))


