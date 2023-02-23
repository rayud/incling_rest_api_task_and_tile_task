from rest_framework import viewsets
from task_app.models import Task, Tile
from task_app.api.serializers import TaskSerializer, TileSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer