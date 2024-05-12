from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from book.models import Book
import rest_framework.views
from test import user
from .models import Order, OrderItem
from .serializers import (OrderCreateSerializer, OrderItemCreateSerializer, OrderItemSerializer,
    OrderSerializer, OrderWriteSerializer, TestOrderSerializer)
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
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserOrderItemListView(ListAPIView):
    serializer_class = OrderSerializer
    # lookup_field = 'userId'
    
    def get_queryset(self):
        userId = self.kwargs.get('pk')
        return Order.objects.filter(userId=userId)
    
class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    
class OrderRetrieveView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderUpdateView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# order item
class OrderItemListView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
class OrderItemCreateView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemCreateSerializer
    
    # def create(self, request, *args, **kwargs):
    #     userId = request.user.id  # Access the current user's ID
    #     order_data = {'userId': userId, 'order_status': 'P'}
    #     order_serializer = OrderCreateSerializer(data=order_data)
    #     order_serializer.is_valid(raise_exception=True)
    #     order = order_serializer.save()

    #     request.data['orderId'] = order.id

    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)

    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
class OrderItemRetrieveView(RetrieveAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
class OrderItemUpdateView(RetrieveUpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
class OrderItemDeleteView(DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    
class OrderWriteView(CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderWriteSerializer 
    
###### test
import logging

logger = logging.getLogger(__name__)

class TestOrderCreateAPIView(CreateAPIView):
    serializer_class = TestOrderSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('userId')  # Assuming user_id is sent in the request data
        book_id = request.data.get('bookId')  # Assuming book_id is sent in the request data
        order_quantity = request.data.get('order_quantity')  # Assuming order_quantity is sent in the request data

        if user_id is None:
            return Response({'message':'userId required'})
        elif book_id is None:
            return Response({'message':'bookId required'})
        
        # Check if the user has an existing order
        # existing_order = Order.objects.filter(userId=user_id, order_status=Order.PENDING).first()
        existing_order = Order.objects.filter(userId=user_id).first()

        if existing_order:
            order = existing_order
        else:
            order = Order.objects.create(userId=user_id)

        # Get the book object or return 404 if not found
        book = get_object_or_404(Book, pk=book_id)

        # Check if book price is None
        if book.price is None:
            logger.error(f"Book price is not set for book {book_id}.")
            return Response({'message': 'Book price is not set'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if order_quantity is None or not a valid number
        try:
            order_quantity = float(order_quantity)
        except (TypeError, ValueError):
            logger.error(f"Invalid order quantity: {order_quantity}")
            return Response({'message': 'Invalid order quantity'}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate total amount and update order
        total_amount = order.total_amount + (book.price * order_quantity)
        order.total_amount = total_amount
        order.save()

        # Create order item
        OrderItem.objects.create(orderId=order, bookId=book, order_quantity=order_quantity)

        return Response({'message': 'Order created successfully'}, status=status.HTTP_201_CREATED)