from django.shortcuts import render
from . import models

def home(request):
    ady = models.Category.objects.all()
    return render(request, 'home.html')
