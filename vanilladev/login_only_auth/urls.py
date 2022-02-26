from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='login'

urlpatterns = [
    path(
        'login/',auth_views.LoginView.as_view(template_name='login_only_auth/login.html'),
    ),
]