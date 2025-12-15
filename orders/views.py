from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from .models import Coupon

class CouponValidationView(APIView):
    def post(self,request):
        code = request.data.get('code')
        today = now().date()

        try:
            coupon = Coupon.objects.get(
                code = code,
                is_active = True,
                valid_from__lte = today,
                valid_until__gte = today
            )
            return Response({
                "valid":True,
                "discount_percentage":coupon.discount_percentage
            })
        except Coupon.DoesNotExist:
            return Response(
                {"valid":False,"error":"Invalid or expired coupon"},
                status = status.HTTP_400_BAD_REQUEST
            )