from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Todo

class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo', 'deadline']

def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    tasks = Todo.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'form': form, 'tasks': tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    task.delete()
    return redirect('/')

def edit_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {
        'form': form,
        'task_id': task_id,
        'current_task': task.todo
    })

def mark_done(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    task.completed = True
    task.save()
    return redirect('/')
