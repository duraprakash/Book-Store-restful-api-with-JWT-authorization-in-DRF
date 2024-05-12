from django.urls import path
from .views import (OrderCreateView, OrderDeleteView, OrderItemCreateView, OrderItemDeleteView,
    OrderItemListView, OrderItemRetrieveView, OrderItemUpdateView, OrderListView,
    OrderRetrieveView, OrderUpdateView, TestOrderCreateAPIView, UserOrderItemListView, OrderWriteView)
from .views import TestOrderCreateAPIView


urlpatterns = [
    path('', OrderListView.as_view(), name='orders'),
    path('<int:pk>/userorder/', UserOrderItemListView.as_view(), name='user_order_item_list'), # get specific user order list
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('<int:pk>/', OrderRetrieveView.as_view(), name='order-retrieve'),
    # path('<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),

    path('order-items/', OrderItemListView.as_view(), name='orderitems'),
    path('order-item/create/', OrderItemCreateView.as_view(), name='ordeitem-create'),
    path('order-item/<int:pk>/', OrderItemRetrieveView.as_view(), name='ordeitem-retrieve'),
    path('order-item/<int:pk>/update/', OrderItemUpdateView.as_view(), name='ordeitem-update'),
    path('order-item/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='ordeitem-delete'),
    
    #### test
    path('test/', OrderWriteView.as_view(), name='test'),
    
]

from .testorderbag.testbagview import TestOrderItemBagView

urlpatterns += [
    path('ordertest/', TestOrderItemBagView.as_view(), name='orders'),
    
]