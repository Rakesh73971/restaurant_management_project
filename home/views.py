from django.shortcuts import render
from .models import MenuCategory,MenuItem,IngredientSerializer
from .serailzers import MenuCategorySerializer,MenuItemSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
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


class MenuItemIngredientView(RetrieveAPIView):
    queryset = MenuItem.objects.all()

    def retrieve(self,request,*args,**kwargs):
        menu_item = self.get_object()
        ingredients = menu_item.ingredients.all()

        serializer = IngredientSerializer(ingredients,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

