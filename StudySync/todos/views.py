from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task
from django.http import HttpResponse

# Create your views here.
def home(request):
    tasks = Task.objects.all().order_by('-created_at')
    contest = {'tasks': tasks}

    return render(request, 'todos/home.html', contest)

def task_toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.is_completed=not task.is_completed
        task.save()

    return redirect('todos:home')

def task_create(request):
    error = None
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()

        if title:
            Task.objects.create(
                title=title,
                description=description
            )
            return redirect('todos:home')
        error = "Title cannot be empty."
    
    return render(request, 'todos/task_form.html', {'error': error})
    

def task_update(request, task_id):
    
    task = get_object_or_404(Task, id=task_id)
    error=None
    
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        is_completed = 'is_completed' in request.POST

        if title:
            task.title = title
            task.description = description
            task.is_completed = is_completed
            task.save()
            return redirect('todos:home')
        
        error = "Tittle cannot be empty" 
    
    return render(request, 'todos/task_form.html', {'task': task, 'error': error})


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('todos:home')
    
    return render(request, 'todos/task_confirm_delete.html', {'task': task})