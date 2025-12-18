from django.urls import path
from .views import OrderHistoryAPIView


urlpatterns = [
    path('order-history/', OrderHistoryAPIView.as_view)),
]