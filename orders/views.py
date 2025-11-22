from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon

# Create your views here.

class CouponValidationView(APIView):

    def post(self,request):
        code = request.data.get("code")

        if not code:
            return Response(
                {"error":"Coupon code is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        today = timezone.now().date()

        try:
            coupon = Coupon.objects.get(code=code,is_active=True)
        except Coupon.DoesNotExist:
            return Response({"error":"Invalid or inactive coupon."},status=status.HTTP_400_BAD_REQUEST)

        if not (coupon.valid_from <= today<=coupon.valid_until):
            return Response({"error":"Coupon is not valid on this date."},status=status.HTTP_400_BAD_REQUEST)


        return Response({
            "success":True,
            "code":coupon.code,
            "discount_percentage":coupon.discount_percentage
        },status=status.HTTP_200_OK)

