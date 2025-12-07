from django.shortcuts import render
from .models import MenuCategory,MenuItem
from .serailzers import MenuCategorySerializer,MenuItemSerializer
from rest_framework.generics import ListAPIView
from django.db.models import Q
from .pagination import 

# Create your views here.

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serailzer_class = MenuCategorySerializer

class MenuItemListView(ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        return MenuItem.objects.filter(is_featured=True)





