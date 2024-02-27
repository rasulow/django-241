from django.shortcuts import render
from . import models

def home(request):
    products = models.Product.objects.all().order_by('-id')
    context = {
        'products': products
    }
    return render(request, 'home.html', context)
