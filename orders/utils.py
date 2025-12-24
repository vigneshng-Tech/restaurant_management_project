import string
import secrets
from orders.models import Coupon 


def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits


    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code

def calculate_tip_amount(order_total * tip_percentage):
    """
    Calculate tip amount based on order total and tip percentage.


    :param order_total: Total bill amount (float or decimal)
    :param tip_percentage: Tip percentage (int, e.g. 15 for 15%)
    :return: Tip amount rounded to 2 decimal places

    """
    tip_amount = order_total * (tip_percentage /100)
    return round(tip_amount, 2)