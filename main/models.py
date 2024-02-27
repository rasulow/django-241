from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        db_table='category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        db_table='Product'
        verbose_name='Product'
        verbose_name_plural='Products'
        
    def __str__(self) -> str:
        return self.name