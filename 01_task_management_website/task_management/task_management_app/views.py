from asyncio import tasks
from email import message
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages

def home(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            tasks = Task.objects.all()
            messages.success(request, message=("New item added!"))
            return render(request, template_name="index.html", context={"tasks": tasks})
    else:
        tasks = Task.objects.all()
        return render(request, template_name="index.html", context={"tasks": tasks})

def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, ("Item deleted!"))
    return redirect(to="home")