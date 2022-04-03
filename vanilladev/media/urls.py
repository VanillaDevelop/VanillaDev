from django.urls import path
from . import views

app_name='media'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('overview/', views.overview, name='overview'),
    path('overview/<int:pageno>/', views.overview, name='overview'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
]