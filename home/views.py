from django.shortcuts import render
from .models import MenuCategory,MenuItem
from .serailzers import MenuCategorySerializer,MenuItemSerializer
from rest_framework.generics import ListAPIView
from django.db.models import Q
from .pagination import MenuItemPagination
from rest_framework import viewsets

# Create your views here.

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serailzer_class = MenuCategorySerializer

class MenuItemListView(ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        return MenuItem.objects.filter(is_featured=True)

class MenuItemSearchViewSet(viewsets.ViewSet):
    """
    A Viewset that provides searching for menu items by name.

    """
    pagination_class = MenuItemPagination

    def list(self,request):
        query = request.query_params.get('q','')

        if not query:
            return Response(
                {'error':'Please provide a search query using ?q='},
                status = status.HTTP_400_BAD_REQUEST
            )
        menu_items = MenuItem.objects.filter(name_icontains=query)

        pagination = self.pagination.class()
        result_page = pagination.paginate_queryset(menu_items,request)

        serializer = MenuItemSerializer(result_page,many=True)

        return pagination.get_paginated_response(serializer.data)

