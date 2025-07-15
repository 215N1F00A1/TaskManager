from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all().order_by('-due_date')  # or use 'title' if you prefer

    return render(request, 'tasks/home.html', {'tasks': tasks})

def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.status = request.POST.get('status')
        task.save()
    return redirect('home')
