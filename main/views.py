from django.shortcuts import render, redirect
from . import models

def home(request):
    products = models.Product.objects.all().order_by('-id')
    context = {
        'products': products
    }
    return render(request, 'home.html', context)


def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        price = request.POST.get('price', 0.0)
        models.Product.objects.create(name=name, description=description, price=price)
        return redirect('home')
    return render(request, 'create.html')


def delete_product(request, id):
    product = models.Product.objects.get(id=id)
    product.delete()
    return redirect('home')