from django.shortcuts import render
from .models import MenuCategory
from .serailzers import MenuCategorySerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serailzer_class = MenuCategorySerializer


