from django.urls import path

from . import views

app_name='home'

urlpatterns = [
    path('', views.index, name='index'),
    path('recentprojects/', views.recentprojects, name='recentprojects'),
    path('recentprojects/<int:id>', views.recentprojects, name='recentprojects'),
]