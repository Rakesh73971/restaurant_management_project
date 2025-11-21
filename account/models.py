from django.db import models
from .models import OrderStatus

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey('customer',on_delete=models.CASCADE)
    
    status = models.ForeignKey(
        OrderStatus,
        on_delete = models.SET_NULL,
        null=True,
        blank=True
    )
    total_amount = models.DecimalField(max_digits=10,decimal_place=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Order #{self.id} - {self.customer}"

