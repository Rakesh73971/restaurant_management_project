from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    discount_percentage = models.DecimalField(max_length=5,decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return self.code

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='oders')
    date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"Order {self.id}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(order,related_name='items',on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places2)