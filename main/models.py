from django.db import models    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    
    class Meta:
        db_table='Product'
        verbose_name='Product'
        verbose_name_plural='Products'
        
    def __str__(self) -> str:
        return self.name