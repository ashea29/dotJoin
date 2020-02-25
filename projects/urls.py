from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('projects/new', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit', views.project_edit, name='project_edit'),
    path('projects/<int:pk>/delete', views.project_delete, name='project_delete'),
]