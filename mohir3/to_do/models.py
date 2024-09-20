from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class LevelModel(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'level'
        verbose_name_plural = 'levels'

class TaskMdoel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    is_active = models.BooleanField(default=False)
    level = models.ForeignKey(LevelModel, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
    
