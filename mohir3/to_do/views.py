from django.shortcuts import render
from .models import TaskMdoel
# Create your views here.

def home_view(request):
    tasks = TaskMdoel.objects.filter(is_active = False).order_by('-created_at')
    
    return render(request, 'home.html', context={'tasks': tasks})

