from .models import MenuCategory
from rest_framework import serializers 

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['name']