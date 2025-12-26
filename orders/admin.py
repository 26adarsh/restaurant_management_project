from django.contrib import admin
from .models import Order, OrderStatus
# Register your models here.

def mark_orders_processed(modeladmin,request,queryset):
    try:
        processed_status = OrderStatus.objects.get(name='Processed')
        queryset.update(status=processed_status)
    except OrderStatus.DoesNotExist:
        modeladmin.message_user(
            request,
            "Processed status does not exist. Please create it first.",
            level='error'
        )

mark_orders_processed.short_description="mark selected orders as Processed"

@admin.register(Order)
class OrderAdmin(admin.modelAdmin):
    list_display = ('id','user','status','created_at')
    list_filter = ('status','created_at')
    actions = [mark_orders_processed]
