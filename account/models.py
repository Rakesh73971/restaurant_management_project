from django.db import models
from .models import OrderStatus

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

    

