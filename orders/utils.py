from django.db.models import Sum
from .models import Order

def get_daily_sales_total(date):
    """
    Returns the total sales amount for a specific  date.
    :param date:datetime.date object
    :return:Decimal or 0
    """
    orders = Order.objects.filter(created_at_date=date)
    total = orders.aggregate(total_amount=Sum('total_price'))['total_sum']

    return total if total if not None else 0
