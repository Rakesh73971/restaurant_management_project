from django.db import models
from .models import OrderStatus

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

    
class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    discount_percentage = models.DecimalField(max_digits=5,decimal_places=2)
    is_active = models.Boolean(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return self.code


