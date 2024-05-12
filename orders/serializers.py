from rest_framework import serializers
from user.serializers import UserSerializer
from book.serializers import BookSerializer
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    # bookId = BookSerializer() # show book info in order
    class Meta:
        model = OrderItem
        fields = ['bookId', 'order_quantity'] # this

class OrderItemCreateSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField()
    class Meta:
        model = OrderItem
        fields = ['orderId', 'bookId', 'order_quantity', 'userId'] # this   
    
class OrderSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField() # this
    class Meta:
        model = Order
        fields = ['id', 'userId', 'created_at', 'updated_at', 'order_status', 'books'] # this
            
    def get_books(self, obj): # this
        books = OrderItem.objects.filter(orderId=obj)
        serializer = OrderItemSerializer(instance=books, many=True)
        return serializer.data      

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # fields = '__all__'
        fields = ['userId', 'order_status']
        
    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        return order


class OrderWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class to create order[bag] for current user and order items[book items]
    """
    
    userId = serializers.HiddenField(default=serializers.CurrentUserDefault()) # should match with order model user reference
    order_items = OrderItemSerializer(many=True) # orderitem model has orderId reference so we can get orderitem here
    
    class Meta:
        model = Order
        fields = (
            "id",
            "userId",
            "order_status",
            "total_amount",
            "order_items",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("order_status",) # order_status in order model is set to read only to avoid user override
    
    """
    creating both order and orderitem table at once,
    firstly pop the order_items then create order object
    then, loop through orderitems list to insert in orderitem table
    """
    def create(self, validated_data):
        orders_data = validated_data.pop('order_items') # get orderitem list data
        order = Order.objects.create(**validated_data) # create order
        
        """
        for loop to insert orderitems list in orderitem table,
        and assigning the orderId with created order table      
        """
        for order_data in orders_data:
            OrderItem.objects.create(orderId=order, **order_data)

        return order
        
    def update(self, instance, validated_data):
        orders_data = validated_data.pop("order_items", None)
        orders = list((instance.order_items).all())

        if orders_data:
            for order_data in orders_data:
                order = orders.pop(0)
                order.bookId = order_data.get('bookId', order.orderId)
                order.order_quantity = order_data.get('order_quantity', order.order_quantity)
                order.save()
                
        return instance
                
####### testing
class TestOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class TestOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = '__all__'