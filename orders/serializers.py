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

""" Normal order and order item """
class OrderItemSerializer(serializers.ModelSerializer):
    # bookId = BookSerializer() # show book info in order
    class Meta:
        model = OrderItem
        fields = '__all__'
        # fields = ['bookId', 'order_quantity'] # this

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
        # bookId = self.validated_data['bookId']
        # order_quantity = self.validated_data['order_quantity']        
        
        user = self.context['request'].user # Get the current authenticated user
        
        # Check if the user is authenticated
        if isinstance(user, AnonymousUser):
            raise serializers.ValidationError("User must be authenticated to create an order")

        # Check if an order exists for the user, if not, create one
        order, created = Order.objects.get_or_create(userId=user)

        # Create a new OrderItem using the obtained or created order
        order_item = OrderItem.objects.create(orderId=order, **validated_data)
        
        return order_item
     
# # class OrderItemCreateSerializer(serializers.ModelSerializer):
# #     # userId = serializers.IntegerField()
# #     class Meta:
# #         model = OrderItem
# #         # fields = ['orderId', 'bookId', 'order_quantity', 'userId'] # this   
# #         fields = ['orderId', 'bookId', 'order_quantity'] # this   
    
# class OrderCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'
#         # fields = ['userId', 'order_status']
        
#     def create(self, validated_data):
#         order = Order.objects.create(**validated_data)
#         return order

# class OrderItemWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = ['id', 'orderId', 'bookId', 'order_quantity']
        
# class OrderWriteSerializer(serializers.ModelSerializer):
#     items = OrderItemWriteSerializer(many=True, read_only=True)
#     class Meta:
#         model = Order
#         fields = ['id', 'userId', 'order_status', 'total_amount', 'items']
#         read_only_fields = ['id', 'total_amount']
        
        