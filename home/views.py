from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer,MenuItemSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from .models import MentItem
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response 
from rest_framework import status
from .models import MentItem
from .serializers import IngredientSerializer
from rest_framework.decorators import api_view


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
    
class MentItemIngredientsView(RetrieveAPIView):
    queryset=MentItem.objects.all()

    def retrieve(self,request,*args,**kwargs):
        menu_item=self.get_object()
        ingredients=menu_item.ingredients.all()
        serializer=IngredientSerializer(ingredients,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def menu_items_by_category(request):
    category_name = request.query.params.get('category')

    if not category_name:
        return Response(
            {"error":"category query parameter is required"},
            status=status.HTTP_400_BAD_REQUEST
        )
    items = MentItem.objects.filter(category__name__iexact=category_name)
    serializer=MenuItemSerializer(items,many=True)

    return Response(serializer.data,status=status.HTTP_200_OK)