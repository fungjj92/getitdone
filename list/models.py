from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=300)
    duedate = models.CharField(max_length=20, blank=True, null=True)
    #duedate = models.DateField(null=True, blank=True)
    #change to DateField if want to organize by date later
    completed = models.BooleanField(default=False)
