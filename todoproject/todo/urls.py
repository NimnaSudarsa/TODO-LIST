# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:task_id>/', views.edit_task, name='edit'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('task-added/', views.task_success, name='task_success'),  # Success page
]
