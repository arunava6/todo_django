from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    task_title=models.CharField(max_length=200)
    task_description=models.TextField(blank=True,null=True)
    task_completed=models.BooleanField(default=False)
    task_created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task_title
    

