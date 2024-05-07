from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'password', 'email', 'seller']
        
    def create(self, validated_data):
        # password = validated_data.pop('password')
        seller = validated_data.get('seller')
        user = User.objects.create_user(**validated_data)
        try:
            seller_group = Group.objects.get(name='seller')
            buyer_group = Group.objects.get(name='buyer')
        except Group.DoesNotExist:
            raise serializers.ValidationError("Group not found")
        if seller:
            user.groups.add(seller_group)
        else:
            user.groups.add(buyer_group)
        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'seller']
        
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