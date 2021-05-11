from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('clear_task_list/', views.clear_task_list, name='clear_task_list')
]
