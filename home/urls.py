from django.urls import path
from .views import MenuCategoryListView,MenuItemIngredientsView

urlpatterns = [
    path('menu-categories/',MenuCategoryListView.as_view()),
    path('menu/featured/',featuredMenuItemListView.as_view(),name='featured-menu-items'),
    path('api/menu-items/<int:pk>/ingredients/',MenuItemIngredientsView.as_view(),
    name='menu-item-ingredients'),
    path('menu-items/',menu_items_by_category,name='menu-items-by-category'),
]