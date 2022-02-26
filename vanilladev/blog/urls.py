from django.urls import path

from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('<int:id>', views.post, name='post'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('categories/', views.categories, name='categories')
]