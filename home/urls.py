from django.urls import path
from .views import MenuCategoryViewSet

urlpatterns = [
    path('categories/',MenuCategoryViewSet.as_view(),name="menu-categories")
    
]