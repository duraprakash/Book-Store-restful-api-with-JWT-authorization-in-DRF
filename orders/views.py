from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from book.models import Book
from test import user
from .models import Order, OrderItem
from .serializers import (
    OrderCreateSerializer, 
    OrderItemCreateSerializer, 
    OrderItemSerializer,
    OrderSerializer, 
    OrderWriteSerializer
    )
from rest_framework.generics import(
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView, 
    
    RetrieveUpdateAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404  # Import get_object_or_404

# Create your views here.
class OrderListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderRetrieveView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderUpdateView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        self.perform_destroy(instance)
        return Response({'message':'Order deleted successfully'})
    
class UserOrderItemListView(ListAPIView):
    serializer_class = OrderSerializer
    # lookup_field = 'userId'
    
    def get_queryset(self):
        userId = self.kwargs.get('pk')
        return Order.objects.filter(userId=userId)

# order item
class OrderItemListView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
class OrderItemCreateView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    
class OrderItemRetrieveView(RetrieveAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
class OrderItemUpdateView(RetrieveUpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
class OrderItemDeleteView(DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        self.perform_destroy(instance)
        return Response({'message':'Order item deleted successfully'})
    
### create order for user then add orderitems
class OrderWriteView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderWriteSerializer
    
    def create(self, request, *args, **kwargs):
        def calculate_total_amount(items):
            # Logic to calculate total amount based on items
            total_amount = 0
            for item_data in items:
                book = item_data['bookId']
                total_amount += item_data['order_quantity'] * book.price
            return total_amount
        
        order_data = {
            'userId': request.user.id,
            'total_amount': calculate_total_amount(request.data['items'])
        }
        
        order_serializer = self.get_serializer(data=order_data)
        order_serializer.is_valid(raise_exception=True)
        order = order_serializer.save()
        
        for item_data in request.data['items']:
            item_data['orderId'] = order.id
            item_serializer = OrderItemSerializer(data=item_data)
            item_serializer.is_valid(raise_exception=True)
            item_serializer.save()

        headers = self.get_success_headers(order_serializer.data)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


