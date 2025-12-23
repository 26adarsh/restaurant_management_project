from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer,MenuItemSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from .models import MentItem

# Create your views here.

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class FeaturedMenuItemListView(ListAPIView):
    queryset = MenuItem.objects.filter(is_featured=True)
    serializer_class = MenuItemSerializer

class MenuItemSearchPagination(PageNumberPagination):
    page_size=10
    page_size_query_param='page_size'
    max_page_size=50

class MenuItemSearchViewSet(ReadOnlyModelViewSet):
    serializer_class=MenuItemSerializer
    pagination_class = MenuItemSearchPagination

    def get_queryset(self):
        queryset MenuItem.objects.all()
        query = self.request.query_params.get('search')
        if query:
            queryset=queryset.filter(name__icontains=query)

        return queryset