from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from book.models import Book
from book.serializers import BookSerializer
from orders.serializers import OrderItemSerializer
from orders.models import Order, OrderItem
from .models import Cart, CartItem
from rest_framework.response import Response
from rest_framework import status

""" Normal cart and cartitem """
class CartItemSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = '__all__'
        
    def get_price(self, obj):
        return obj.book.price

    def get_cost(self, obj):
        return obj.cost
    
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'        
""" Normal cart and cartitem """



class CartItemListSerializer(serializers.ModelSerializer):
    # book = serializers.ReadOnlyField(source='book.title')
    # book = serializers.StringRelatedField(read_only=True)
    cost = serializers.FloatField()
    class Meta:
        model = CartItem
        fields = '__all__'
        # fields = ['id', 'book', 'quantity', 'cost']
        # fields = ['id', 'book', 'quantity', 'cost', 'book_details']

    # # Additional fields can be added if needed, e.g., book details
    # book_details = serializers.SerializerMethodField()
    cart_details = serializers.SerializerMethodField()
    def get_cart_details(self, obj):
        return {
            'order_status': obj.cart.order_status,
        }
    def get_book_details(self, obj):
        return {
            'title': obj.book.title,
            # 'author': obj.book.authors,
            'authors': [author.name for author in obj.book.authors.all()],
            'price': obj.book.price,
        }    
    
class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['book', 'quantity']

    def create(self, validated_data):
        user_id = self.context['request'].user
        book_id = self.validated_data['book'].id
        cart_quantity = self.validated_data['quantity']
        
        if isinstance(user_id, AnonymousUser):
            raise serializers.ValidationError('User must be authenticated create an cart')
        
        cart_id, created = Cart.objects.get_or_create(user=user_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart_id, book=book_id, defaults=False)
        
        book = Book.objects.get(id=book_id)
        if cart_quantity > book.stock_quantity:
            raise serializers.ValidationError(f'Only {book.stock_quantity} items are available in stock for {book.title}')
        
        if cart_item:
            cart_item.quantity =  cart_quantity
        else:
            cart_item = CartItem.objects.create(cart=cart_id, **validated_data)
            
        cart_item.save()
        return cart_item

class AddCartToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['bookId', 'order_quantity']

    def create(self, validated_data):        
        # get user input data
        user_id = self.context['request'].user
        book_id = self.validated_data['bookId'].id
        order_quantity = self.validated_data['order_quantity']
        
        if isinstance(user_id, AnonymousUser):
            raise serializers.ValidationError('User must be authenticated create an cart')
        
    
        # check order created for user
        order_id, created = Order.objects.get_or_create(userId=user_id)
        
        order_item = OrderItem.objects.filter(orderId=order_id, bookId=book_id).first()
        
        # check book exist
        book = Book.objects.get(id=book_id)
        
        if order_quantity > book.stock_quantity:
            raise serializers.ValidationError(f'Only {book.stock_quantity} items are available in stock for {book.title}')
        
        if order_item:
            order_item.quantity =  order_quantity
        else:
            # store the user input data in dict
            order_item = OrderItem.objects.create(orderId=order_id, **validated_data) 
            
        order_item.save()
        
        # update the order status in cartitem
        cart = Cart.objects.get(user=user_id)
        cart_items = CartItem.objects.filter(cart=cart, book=book_id)
        for cart_item in cart_items:
            cart_item.ordered = True  # status changed
            cart_item.save()

        # Update the stock quantity of the book
        book.stock_quantity -= order_quantity
        book.save()
        
        return order_item

    
class CartListSerializer(serializers.ModelSerializer):
    book = CartItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cart
        fields = '__all__'        