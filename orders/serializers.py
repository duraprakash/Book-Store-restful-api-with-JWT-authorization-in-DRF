import django.shortcuts
from rest_framework import serializers
from user.serializers import UserSerializer
from book.serializers import BookSerializer
from book.models import Book
from user.models import User
from .models import Order, OrderItem

""" Normal order and order item """
class OrderItemSerializer(serializers.ModelSerializer):
    # bookId = BookSerializer() # show book info in order
    class Meta:
        model = OrderItem
        fields = '__all__'
        # fields = ['bookId', 'order_quantity'] # this

class OrderSerializer(serializers.ModelSerializer):
    # books = serializers.SerializerMethodField() # this
    class Meta:
        model = Order
        fields = '__all__'
        # fields = ['id', 'userId', 'created_at', 'updated_at', 'order_status', 'books'] # this
        # fields = ['id', 'userId', 'created_at', 'updated_at', 'order_status'] # this
            
""" Normal order and order item """


    # def get_books(self, obj): # this
    #     books = OrderItem.objects.filter(orderId=obj)
    #     serializer = OrderItemSerializer(instance=books, many=True)
    #     return serializer.data     
     
class OrderItemCreateSerializer(serializers.ModelSerializer):
    # userId = serializers.IntegerField()
    class Meta:
        model = OrderItem
        # fields = ['orderId', 'bookId', 'order_quantity', 'userId'] # this   
        fields = ['orderId', 'bookId', 'order_quantity'] # this   
    
class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        # fields = ['userId', 'order_status']
        
    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        return order

class OrderItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'orderId', 'bookId', 'order_quantity']
        
class OrderWriteSerializer(serializers.ModelSerializer):
    items = OrderItemWriteSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'userId', 'order_status', 'total_amount', 'items']
        read_only_fields = ['id', 'total_amount']
        
        