from django.urls import path
from .views import home_view,delete_view, task_view



urlpatterns = [
    path("", home_view, name='home'),
    path("delete/<int:id>/", delete_view, name="delete"),
    path("task/<int:id>/", task_view, name="task_view")
]