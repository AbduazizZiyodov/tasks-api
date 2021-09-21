from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import RetrieveAPIView

from .models import Task

from .serializers import TaskSerializer
from .serializers import TaskListSerializer

from .permissions import *


class ListTasks(ListAPIView):
    permission_classes = [CanRead]
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TaskDetail(RetrieveAPIView):
    permission_classes = [CanRead]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTask(CreateAPIView):
    permission_classes = [CanCreate]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UpdateTask(UpdateAPIView):
    permission_classes = [CanUpdate]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DeleteTask(DestroyAPIView):
    permission_classes = [CanDelete]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


tasks, create_task, update_task, delete_task, task_detail = \
    ListTasks.as_view(), CreateTask.as_view(), UpdateTask.as_view(),\
    DeleteTask.as_view(), TaskDetail.as_view()


__all__: list = [
    "tasks", "create_task", "update_task",
    "delete_task", "task_detail"
]
