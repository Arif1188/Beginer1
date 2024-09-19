from django.urls import path, include
from .views import home,product_detail_view, product_delete_view

urlpatterns = [
    path("", home, name='home'),
    path("detail/<int:id>/",product_detail_view, name='detail'),
    path("delete/<int:id>/",product_delete_view, name='delete')
]