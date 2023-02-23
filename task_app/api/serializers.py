from rest_framework import serializers
from task_app.models import Task,Tile

class TaskSerializer(serializers.ModelSerializer):
    # tile = serializers.CharField(source='tile.name')
    class Meta: 
        model = Task 
        fields = '__all__'

class TileSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta: 
        model = Tile 
        fields = '__all__'