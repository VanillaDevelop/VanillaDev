from django.urls import path
from django.contrib.auth import views as auth_views
from ratelimit.decorators import ratelimit

app_name='login'

urlpatterns = [
    path('login/', ratelimit(key='ip', method='POST', rate="3/10m", block=True)(auth_views.LoginView.as_view(template_name='login_only_auth/login.html', redirect_authenticated_user=True)), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout')
]