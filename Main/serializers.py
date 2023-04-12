from .models import Cart, Order, OrderItem,  Item, Category
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'



class ManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = User.objects.create(**validated_data)
        user.groups.add(Group.objects.get(name='Manager'))
        user.is_staff = True
        user.save()
        return user


class DeliveryCrewSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = User.objects.create(**validated_data)
        user.groups.add(Group.objects.get(name='DeliveryCrew'))
        return user
