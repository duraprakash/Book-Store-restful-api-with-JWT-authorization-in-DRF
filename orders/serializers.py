import django.shortcuts
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from user.serializers import UserSerializer
from book.serializers import BookSerializer
from book.models import Book
from user.models import User
from .models import Order, OrderItem
from django.contrib.auth.models import AnonymousUser
from rest_framework.exceptions import ValidationError

""" Normal order and order item """
class OrderItemSerializer(serializers.ModelSerializer):
    # bookId = BookSerializer() # show book info in order
    price = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        # fields = '__all__'
        fields = ['orderId', 'bookId', 'order_quantity', 'price', 'cost']
        
    def get_price(self, obj):
        return obj.bookId.price

    def get_cost(self, obj):
        return obj.cost

class OrderSerializer(serializers.ModelSerializer):
    # books = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = '__all__'
        # fields = ['id', 'userId', 'created_at', 'updated_at', 'order_status', 'books']
    
    # def get_books(self, obj):
    #     books = OrderItem.objects.filter(orderId=obj)
    #     serializer = OrderItemSerializer(instance=books, many=True)
    #     return serializer.data   
""" Normal order and order item """


class UserOrderItemSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField() # this
    class Meta:
        model = Order
        # fields = '__all__'
        # fields = ['id', 'userId', 'order_status'] # limited fields shown
        fields = ['id', 'userId', 'created_at', 'updated_at', 'order_status', 'books'] # this
        
        
    def get_books(self, obj): # this
        books = OrderItem.objects.filter(orderId=obj)
        serializer = OrderItemSerializer(instance=books, many=True)
        return serializer.data     

class OrderItemCartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['bookId', 'order_quantity']
    
    def create(self, validated_data):
        # # how to get user input data in serializers
        # userId = self.validated_data['userId']
        book_id = self.validated_data['bookId'].id # foreign key id
        order_quantity = self.validated_data['order_quantity']        
        
        user = self.context['request'].user # Get the current authenticated user
        
        if isinstance(user, AnonymousUser):
            raise serializers.ValidationError("User must be authenticated to create an order")

        order, created = Order.objects.get_or_create(userId=user)
        
        # Check if the book item already exist in the user's order
        order_item = OrderItem.objects.filter(orderId=order, bookId=book_id).first()
        
        book = Book.objects.get(id=book_id)
        if order_quantity > book.stock_quantity:
            raise ValidationError(f"Only {book.stock_quantity} items are available in stock for {book.title}")

        if order_item:
            order_item.order_quantity = validated_data['order_quantity']
            order_item.save()
        else:
            # If the book is not in the order, create a new OrderItem using the obtained or created order
            order_item = OrderItem.objects.create(orderId=order, **validated_data)
        
        # Update the stock quantity of the book
        book.stock_quantity -= order_quantity
        book.save()
        
        return order_item