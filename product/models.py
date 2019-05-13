from django.conf import settings
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)    
    price = models.FloatField()
    weight = models.FloatField()
    description = models.TextField()    

    def details(self,price):
        self.price=price
    
    def __str__(self):
        return self.name
