from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework.permissions import ISAuthenticated
from.models import Order
from.serializers import OrderSerializer

class OrderHistoryAPIView(APIView)
    permissions_classes = [ISAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
