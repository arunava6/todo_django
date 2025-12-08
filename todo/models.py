from django.db import models

# Create your models here.

class Task(models.Model):
    task_title=models.CharField(max_length=200)
    task_description=models.TextField(blank=True,null=True)
    task_completed=models.BooleanField(default=False)
    task_created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task_title
    

