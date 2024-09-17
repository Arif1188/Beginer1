from django.shortcuts import render
from .models import StudendModel

# Create your views here.

def home(request):
    queryset = StudendModel.objects.all()
    return render(request, 'home.html', context={'students':queryset})

def base(request):
    return render(request, 'base.html')