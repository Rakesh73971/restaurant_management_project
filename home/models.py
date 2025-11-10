from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    status = models.Foreignkey(OrderStatus, on_delete=models.SET_NULL,null=True)

