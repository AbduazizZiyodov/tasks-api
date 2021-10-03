from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework.permissions import AllowAny

from .models import Task

from .serializers import TaskSerializer
from .serializers import TaskListSerializer

from .permissions import *


class ListTasks(ListAPIView):
    permission_classes = [CanRead]
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class CreateTask(CreateAPIView):
    permission_classes = [CanCreate, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailed(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        permissions: dict[str, tuple] = {
            "GET": (CanRead(),),
            "PUT": (CanUpdate(),),
            "PATCH": (CanUpdate(),),
            "DELETE": (CanDelete(),)
        }
        return permissions.get(self.request.method, (AllowAny(),))


tasks, create_task, task_detailed = \
    ListTasks.as_view(), CreateTask.as_view(), TaskDetailed.as_view()


__all__: list = [
    "tasks", "create_task", "task_detailed",
]
