from django.urls import path
from .views import home, base

urlpatterns = [
    path('', home),
    path('base/', base, name='base/')
]