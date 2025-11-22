from django.urls import path
from .views import *

urlpatterns = [
    path("coupons/validate/",CouponValidateView.as_view(),name="coupon-validate")
    
]