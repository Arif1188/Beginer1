from django.shortcuts import render,redirect
from .models import TaskModel

def home_view(request):
    q = request.GET.get('q')
    tasks = TaskModel.objects.filter(is_active = False).order_by('-created_at')
    if q:
        tasks = tasks.filter(title__icontains=q)
    return render(request, 'home.html', context={'tasks':tasks})

def delete_view(request,id):
    TaskModel.objects.get(id=id).delete()
    return redirect("home", )

def task_view(request, id):
    task = TaskModel.objects.get(id=id)
    return render(request, 'view_task.html', context={'task': task})
    
