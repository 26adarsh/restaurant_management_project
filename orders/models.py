from django.db import models

# Create your models here.
from .models import OrderStatus

class Order(models.Model):
    status = models.ForeignKey(
        OrderStatus,
        on_delete = models.SET_NULL,
        null = True
    )

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