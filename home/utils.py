from datetime import datetime,time
import re
from email.utils import parseaddr
import logging

logger = logging.getLogger(__name__)

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

def is_valid_email(email:str)->bool:
    try:
        if not email:
            return False
        name,addr = parseaddr(email)
        if '@' not in addr:
            return False

        local_part,domain=addr.split('@',1)

        if not local_part or not domain:
            return False
        if '.' not in domain:
            return False
        return True

    except Exception as e:
        logger.error(f"Email validation error:{e}")
        return False