from django.db import models

# Create your models here.
from .models import OrderStatus

class Order(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('processing','Processing'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    ]
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    
    objects=ActiveOrderManager()
    def __str__(self):
        return f"Order #{self.id}-{self.status}"

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique = True)

    def __str__(self):
        return self.name

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    is_active = models.BooleanField()
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return self.code

class Restaurant(models.Model):
    name = models.CharField(max_length = 255)
    address = models.TextField()
    has_delivery = models.BooleanField(default=False)

class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__in=['pending','processing'])
