from django.urls import path
from .views import MenuCategoryListView

urlpatterns = [
    path('menu-categories/',MenuCategoryListView.as_view()),
    path('menu/featured/',featuredMenuItemListView.as_view(),name='featured-menu-items'),
]