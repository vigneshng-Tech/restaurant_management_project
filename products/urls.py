from django.urls import path
from .views import ItemView, ItemSearchView

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('items/search/', ItemSearchView.as_view(), name='item-search'),
]