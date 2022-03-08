from django.urls import path
from . import views

app_name='projects'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('overview/', views.overview, name='overview'),
    path('<int:id>', views.page, name='page'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete')
]