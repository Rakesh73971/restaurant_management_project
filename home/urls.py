from django.urls import path
from .views import MenuCategoryListView,MenuItemListView

urlpatterns = [
    path('categories/',MenuCategoryListView.as_view(),name="menu-categories")
    path('featured-menu-items',MenuItemListView.as_view(),name='featured-menu-items')
]