from django.urls import path
from .views import CouponValidationView, OrderHistoryView,OrderDetailView


urlpatterns = [
    path('coupons/validate/',CouponValidationView.as_view()),
    path('orders/history/',OrderHistoryView.as_view(),name,name='order-history'),
    path('orders/<int:pk>/',OrderDetailView.as_view(),name='order-detail'),
]