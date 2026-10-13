from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.task_create, name='task_create'),
    path('toggle/<int:task_id>/', views.task_toggle_complete, name='task_toggle'),
    path('edit/<int:task_id>/', views.task_update, name='task_update'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
]