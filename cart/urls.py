from django.urls import path
from .views import *

urlpatterns = [
    path('', CartListAPIView.as_view(), name='cart-items-list'),
    path('create/', CartItemCreateAPIView.as_view(), name='add-to-cart'),
    path('cart-to-order/', AddCartToOrder.as_view(), name='add-to-cart'),
    path('<int:pk>/retrieve/', CartDetailAPIView.as_view(), name='cart-item'),
    path('<int:pk>/delete/', CartItemDeleteAPIView.as_view(), name='delete-cart-item'),
]
