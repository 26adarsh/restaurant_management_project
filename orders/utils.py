import string
import secrets
from orders.models import Coupon
from datetime import datetime
from .models import DailyOperatingHours,Order
from django.db.models import Sum
from decimal import Decimal,ROUND_HALF_UP


def generate_coupon_code(length=10):
    characters = string.ascii_uppercase+string.digits

    while True:
        code=''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code

def get_today_operating_hours():
    today = datetime.now().strftime('%A')
    try:
        hours = DailyOperatingHours.objects.get(day=today)
        return hours.open_time,hours.close_time
    except DailyOperatingHours.DoesNotExist:
        return None, None

def get_daily_sales_total(date):
    result = Order.objects.filter(
        created_at__date=date
    ).aggregate(total_sum=Sum('total_price'))
    return result['total_sum'] or 0

def calculate_tip_amount(order_total,tip_percentage):
    order_total=Decimal(str(order_total))
    tip_percentage=Decimal(str(tip_percentage))
    tip_amount=order_total*(tip_percentage/Decimal('100'))
    return tip_amount.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)