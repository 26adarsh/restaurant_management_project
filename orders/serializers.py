from rest_framework import serializers
from .models import Order,OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','item','quantity','price']

class OrderItemSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)

    class Meta:
        model = Order
        fields = ['id','created_at','total_price','items']

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields=[
            'id','status','total_price','created_at','user','customer'
        ]