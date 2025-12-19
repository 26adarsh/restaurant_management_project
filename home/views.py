from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer,MenuItemSerializer
# Create your views here.

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class FeaturedMenuItemListView(ListAPIView):
    queryset = MenuItem.objects.filter(is_featured=True)
    serializer_class = MenuItemSerializer
