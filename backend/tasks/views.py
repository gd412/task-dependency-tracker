from rest_framework import viewsets
from .models import Task, TaskDependency
from .serializers import TaskSerializer, TaskDependencySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDependencyViewSet(viewsets.ModelViewSet):
    queryset = TaskDependency.objects.all()
    serializer_class = TaskDependencySerializer
