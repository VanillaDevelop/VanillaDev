"""vanilladev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('user/', include('login_only_auth.urls', namespace='user')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('media/', include('media.urls',namespace='media')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('articles/', include('articles.urls', namespace='articles')),
    path('side/', include('sideprojects.urls', namespace='sideprojects')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
