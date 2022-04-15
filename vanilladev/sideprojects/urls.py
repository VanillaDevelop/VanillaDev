from django.urls import path
from . import views

app_name='sideprojects'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('overview/', views.overview, name='overview'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete')
]