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

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    has_delivery = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class DailySpecial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='specials/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    @staticmethod
    def get_random_special():
        """ 
        Returns a random DailySpecial object.
        If none exist, returns None.
        """
        specials = DailySpecial.objects.order_by('?')
        return specials.first() if specials.exists() else None

    def __str__(self):
        return self.title