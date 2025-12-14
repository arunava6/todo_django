from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists!")
            return redirect("/register/")

        user = User.objects.create(
            first_name=first_name, last_name=last_name, email=email
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully!.")
        return redirect("/login/")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        password = data.get("password")

        try:
            user_obj = User.objects.get(email=email)
        except:
            messages.warning(request, "Email not exists")
            return redirect("/login/")

        user = authenticate(request, username=user_obj.username, password=password)

        if user is None:
            messages.warning(request, "Invalid password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")


@login_required(login_url="/login/")
def add_task(request):
    if request.method == "POST":
        data = request.POST
        task_title = data.get("task_title")
        task_description = data.get("task_description")
        task_completed = True if data.get("task_completed") == "on" else False

        Task.objects.create(
            task_title=task_title,
            task_description=task_description,
            task_completed=task_completed,
        )

        return redirect("/")

    queryset = Task.objects.all()
    context = {"tasks": queryset}

    return render(request, "home.html", context)


@login_required(login_url="/login/")
def update_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        if "task_completed" in data and "task_title" not in data:
            task.task_completed = True
            task.save()
            return redirect("/")

        task.task_title = data.get("task_title")
        task.task_description = data.get("task_description")
        task.task_completed = True if data.get("task_completed") == "on" else False

        task.save()
        return redirect("/")

    return render(request, "update.html", {"task": task})


@login_required(login_url="/login/")
def delete_task(request, id):
    if request.method=="POST":
        queryset = Task.objects.get(id=id)
        queryset.delete()
    return redirect("/")

