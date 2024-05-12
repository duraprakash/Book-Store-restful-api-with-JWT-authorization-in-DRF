from rest_framework import generics
from orders.models import Order
from orders.testorderbag.testserializers import TestOrderItemBagSerializer

class TestOrderItemBagView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = TestOrderItemBagSerializer
    