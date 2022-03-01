from django.urls import path

from . import views

app_name='blog'

urlpatterns = [
    path('', views.overview, name='overview'),
    path('<int:pageno>', views.overview, name='overview'),
    path('post/<int:id>', views.post, name='post'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('categories/', views.categories, name='categories'),
    path('delete/<int:id>', views.delete, name='delete')
]