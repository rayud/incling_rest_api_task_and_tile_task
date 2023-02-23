from django.db import models

class Tile(models.Model):
    name = models.CharField(max_length=100)
    launch_date = models.DateField()
    TILE_STATUS_CHOICES = [
        ('live', 'Live'),
        ('pending', 'Pending'),
        ('archived', 'Archived')
    ]
    status = models.CharField(max_length=20, choices=TILE_STATUS_CHOICES)
    
    def __str__(self):
        return self.name 
    
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField()
    description = models.TextField()
    TASK_TYPE_CHOICES = [
        ('survey', 'Survey'),
        ('discussion', 'Discussion'),
        ('diary', 'Diary')
    ]
    task_type = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES)
    tile = models.ForeignKey('Tile', on_delete=models.CASCADE, related_name='tasks')
    
    def __str__(self):
        return self.title