from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from views import IndexView
app_name = 'accounts'
urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
