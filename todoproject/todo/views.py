# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_success')  # Redirect to success page
    return render(request, 'todo/index.html', {'tasks': tasks, 'form': form})

@login_required
def task_success(request):
    return render(request, 'todo/success.html')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('/')

@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('/')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/edit.html', {'form': form, 'task': task})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/login/')
