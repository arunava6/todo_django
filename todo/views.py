from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def add_task(request):
    if request.method=="POST":
        data=request.POST
        task_title=data.get("task_title")
        task_description=data.get("task_description")
        task_completed=True if data.get("task_completed") == "on" else False

        Task.objects.create(
            task_title=task_title,
            task_description=task_description,
            task_completed=task_completed,
        )

        return redirect("/")
    
    queryset=Task.objects.all()
    context={'tasks':queryset}

    return render(request,"home.html",context)


def update_task(request,id):
    queryset=Task.objects.get(id=id)

    if request.method=="POST":
        data=request.POST
        task_title=data.get("task_title")
        task_description=data.get("task_description")
        task_completed = True if data.get("task_completed") == "on" else False

        queryset.task_title=task_title
        queryset.task_description=task_description
        queryset.task_completed=task_completed

        queryset.save()

        return redirect("/")
    
    context={'task':queryset}
    return render(request,"update.html",context)


def delete_task(request,id):
    queryset=Task.objects.get(id=id)
    queryset.delete()
    return redirect("/")


