from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    status = models.Foreignkey(OrderStatus, on_delete=models.SET_NULL,null=True)
    
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

