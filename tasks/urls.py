from django.urls import path

from .views import *

urlpatterns: list = [
    path('api/tasks', tasks,name="List of all tasks"),
    
    path(
        'api/tasks/create', create_task,
        name='You can create New Task'
    ),

    path(
        'api/tasks/<int:pk>', task_detailed,
        name='You can perform actions at Task by its pk'
    ),
]
