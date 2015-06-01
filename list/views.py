from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

#Create your views here.

#Via JS/JQuery/HTML/CSS, entered tasks are displayed
#to the index but no changes made to backend. Thus refresh
#wipes that data. Python/Django to resolve this, adding DB.

def index(request):
    tasks = Task.objects.all()
    return render(request, "list/list.html", {'tasks': tasks})

#backend begins
@csrf_exempt
def addTask(request):
    #add task to db if form submitted
    if request.method == 'POST':
        newtask = request.POST.get('task')
        duedate = request.POST.get('duedate')
        createdTask = Task.objects.create(task=newtask, duedate=duedate)
        return JsonResponse({'id': createdTask.id, 'task': createdTask.task, 'duedate': createdTask.duedate, 'completed': createdTask.completed})

@csrf_exempt
def completeTask(request):
    #update completion status in db if task clicked in DOM
    id = getID(request)
    task = Task.objects.get(id=id)
    if task.completed == False:
        task.completed = True
    else:
        task.completed = False
    task.save()
    return JsonResponse({'id': task.id, 'task': task.task, 'duedate': task.duedate, 'completed': task.completed})

@csrf_exempt
def deleteTask(request):
    #delete task in db if clicked in DOM
    id = getID(request)
    task = Task.objects.get(id=id)
    task.delete()
    return JsonResponse({'id': task.id, 'deleted': True})

def getID(request):
    if request.method == 'POST':
        return int(request.POST.get('id'))
    else:
        return None


#maybe later: update db position if rearranged (switch id #)
