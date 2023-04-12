from django.shortcuts import render
from rest_framework import generics, status
from .models import OrderItem, Item, Cart, Order, Category
from .serializers import OrderSerializer, OrderItemSerializer, ItemSerializer, CartSerializer, CategorySerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from .permissions import IsAllowedEditOrReadOnly, IsManager
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .serializers import ManagerSerializer, DeliveryCrewSerializer

# Create your views here.


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
# all menu items


class ItemView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAllowedEditOrReadOnly]
    ordering_fields = ['title', 'price']
    search_fields = ['title']

# single menu item


class SingleItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAllowedEditOrReadOnly]


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

class ManagersView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name__contains='Manager')
    serializer_class = ManagerSerializer
    permission_classes = [IsManager]

class SingleManagerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(groups__name__contains='Manager')
    serializer_class = ManagerSerializer
    permission_classes = [IsManager]

class DeliveryCrewsView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name__contains='DeliveryCrew')
    serializer_class = DeliveryCrewSerializer
    permission_classes = [IsManager]

class SingleDeliveryCrewView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(groups__name__contains='DeliveryCrew')
    serializer_class = DeliveryCrewSerializer
    permission_classes = [IsManager]


