from django.urls import path
from . import views

app_name='media'

urlpatterns = [
    path('add/', views.add, name='add'),
]