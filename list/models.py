from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

#Represents a user's list of entered tasks
class List(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=50)

    def __init__(self, user, name):
        self.owner = user
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

class Task(models.Model):
    task = models.CharField(max_length=300)
    duedate = models.DateField()
    list = models.ForeignKey(List)

    def __init__(self, task, date, list, duedate = ""):
        self.task = task
        self.duedate = date
        self.list = list

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'duedate', 'list']

''' class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ['user', 'name']'''


#
## Change such that tasks are assigned list value of current list
## rather than array of tasks in any list
#