from datetime import datetime,time
import re

def is_restaurant_open():
    now = datetime.now()
    current_time = now.time()
    current_day = now.weekday()

    if current_day < 5:
        open_time = time(9,0)
        close_time = time(22,0)
    else:
        open_time=time(10,0)
        close_time=time(23,0)
    return open_time <= current_time<=close_time

def is_valid_phone_number(phone_number:str)->bool:
    pattern = r'^(\+\d{1,3}[\s-]?)?\d{3,4}[\s-]?\d{3,4}[\s-]?\d{3,4}$'
    return bool(re.match(pattern,phone_number))