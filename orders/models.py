from django.db import models

# Create your models here.
from .models import OrderStatus

class Order(models.Model):
    status = models.ForeignKey(
        OrderStatus,
        on_delete = models.SET_NULL,
        null = True
    )
