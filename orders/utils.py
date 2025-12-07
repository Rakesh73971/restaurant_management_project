from django.db.models import Sum
from .models import Order
from decimal import Decimal

def get_daily_sales_total(date):
    """
    Returns the total sales amount for a specific  date.
    :param date:datetime.date object
    :return:Decimal or 0
    """
    orders = Order.objects.filter(created_at_date=date)
    total = orders.aggregate(total_amount=Sum('total_price'))['total_sum']

    return total if total if not None else 0


def calculate_tip_amount(order_total,tip_percentage):
    """
    Calculate the tip amount based on the order total and tip percentage.
    Parameters:
       order_total (Decimal or float): The total bill amount before tip.
       tip_percentage: The tip percentage (e.g: 15 for 15%).
    Returns:
        Decimal:The calculated tip amount rounded to two decimal places.
    """
    total = Decimal(order_total)
    percentage = Decimal(tip_percentage)/Decimal(100)
    tip_amount = total * percentage

    return round(tip_amount,2)