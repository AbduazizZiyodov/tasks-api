from django.urls import path

from .views import *

urlpatterns: list = [
    path('api/tasks', tasks,name="List of all tasks"),
    
    path(
        'api/tasks/create', create_task,
        name='You can create New Task'
    ),

    path(
        'api/tasks/<int:pk>', task_detail,
        name='You can get Task by its pk'
    ),

    path(
        'api/tasks/<int:pk>/update', update_task,
        name="You can update Task by its pk"
    ),

    path(
        'api/tasks/<int:pk>/delete', delete_task,
        name="You can delete Task by its pk"
    ),
]
