import orders.testorderbag.testserializers
from rest_framework import serializers
from orders.models import Order, OrderItem

class TestOrdeBagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class TestOrderItemBagSerializer(serializers.ModelSerializer):
    orderId = TestOrdeBagSerializer()
    class Meta:
        model = OrderItem
        # fields = '__all__'
        fields = ['orderId']