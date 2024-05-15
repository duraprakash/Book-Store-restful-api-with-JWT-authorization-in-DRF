from django.urls import path
from .views import (OrderCreateView, OrderDeleteView, OrderItemCreateView, OrderItemDeleteView,
    OrderItemListView, OrderItemRetrieveView, OrderItemUpdateView, OrderItemWriteView,
    OrderListView, OrderRetrieveView, OrderUpdateView,  UserOrderItemListView)

urlpatterns = [
    # order
    path('', OrderListView.as_view(), name='orders'),
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('<int:pk>/', OrderRetrieveView.as_view(), name='order-retrieve'),
    path('<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),

    # order-item
    path('order-items/', OrderItemListView.as_view(), name='orderitems'),
    path('order-item/create/', OrderItemCreateView.as_view(), name='ordeitem-create'),
    path('order-item/<int:pk>/', OrderItemRetrieveView.as_view(), name='ordeitem-retrieve'),
    path('order-item/<int:pk>/update/', OrderItemUpdateView.as_view(), name='ordeitem-update'),
    path('order-item/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='ordeitem-delete'),
    
    
    path('<int:pk>/userorder/', UserOrderItemListView.as_view(), name='user_order_item_list'), # get specific user order list
    
    path('order-item/create-cart/', OrderItemWriteView.as_view(), name='ordeitemcreate'), # order and order-item at once
    
    # path('orderitem/create/', OrderWriteView.as_view(), name='ordeitemcreate'),
    
]