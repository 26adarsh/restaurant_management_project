import string
import secrets
from orders.models import Coupon
from datetime import datetime
from .models import DailyOperatingHours

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