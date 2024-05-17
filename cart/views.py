from rest_framework import generics, permissions
from cart.models import Cart, CartItem
from cart.serializers import (AddCartToOrderSerializer, CartItemCreateSerializer,
    CartItemListSerializer, CartItemSerializer, CartListSerializer, CartSerializer)
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CartListAPIView(generics.ListAPIView):
    serializer_class = CartItemListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        cart = Cart.objects.get(user=user)
        return CartItem.objects.filter(cart=cart)
    
class CartDetailAPIView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Cart.objects.get(user=self.request.user)

class CartItemCreateAPIView(generics.CreateAPIView):
    # queryset = Cart.objects.all()
    serializer_class = CartItemCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

class AddCartToOrder(generics.CreateAPIView):
    serializer_class = AddCartToOrderSerializer
    permission_classes = [permissions.IsAuthenticated]
        
class CartItemDeleteAPIView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)