from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def listPage(request):
    if request.method == 'POST':
        newtask = request.POST.get('newtask')
        date = request.POST.get('date')
        Task.objects.create(task=newtask, date=date, list="to-do")

    return render(request, "list/list.html")

    # Add, delete, move tasks
