from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_product, name='create'),
    path('delete/<int:id>/', views.delete_product, name='delete'),
]