from django.shortcuts import render,redirect
from .models import ProductModel

# Create your views here.
def home(request):
    products = ProductModel.objects.all()
    context = {'products':products}
    return render(request, 'home.html', context=context)

def product_detail_view(request, id):
    product_obj = ProductModel.objects.get(id=id)
    return render(request, 'product_detail.html', context={'product':product_obj})

def product_delete_view(request,id):
    product_obj = ProductModel.objects.get(id=id).delete()
    return redirect('home')