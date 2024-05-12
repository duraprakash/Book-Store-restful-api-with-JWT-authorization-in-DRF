from rest_framework import serializers
from .models import Address, Geo, User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = '__all__'
        
class AddressSerializer(serializers.ModelSerializer):
    # geo = GeoSerializer()
    class Meta:
        model = Address
        fields = '__all__'
    
    # def create(self, validated_data):
    #     geo_data = validated_data.pop('geo') # remove from dic
    #     geo = Geo.objects.create(**geo_data) # transform into dic
    #     address = Address.objects.create(geo=geo, **validated_data) # insert
    #     return address
        
class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    # pasword = serializers.CharField()
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'password', 'email', 'seller', 'address']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

        
    def create(self, validated_data):
        # remove from dic
        address_data = validated_data.pop('address')
        
        # transform into dic
        address = Address.objects.create(**address_data)
        
        user = User.objects.create_user(**validated_data)
        
        # Assign user to seller or buyer group based on 'seller' flag
        seller = validated_data.get('seller', False)
        if seller:
            group_name = 'seller'
        else:
            group_name = 'buyer'
        
        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            # raise serializers.ValidationError("Group not found")
            sellers = ['seller', 'buyer']
            for i in sellers:
                group = Group.objects.create(name=i) # add buyer and seller if not exists but permission not assign yet
        
        user.address = address
        user.groups.add(group)
        user.save()
        
        return user        

class UserListSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'seller', 'address']

class UserUpdateSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'seller', 'address']

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        if address_data:
            address_instance = instance.address
            for key, value in address_data.items():
                setattr(address_instance, key, value)
            address_instance.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance 
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    
