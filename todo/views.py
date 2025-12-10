from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        data=request.POST
        first_name=data.get("first_name")
        last_name=data.get("last_name")
        email=data.get("email")
        password=data.get("password")

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists!")
            return redirect("/register/")
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully!.")
        return redirect("/register/")
    
    return render(request,"register.html")


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


# for updating the task
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


