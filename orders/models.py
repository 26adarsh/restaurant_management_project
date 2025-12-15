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
