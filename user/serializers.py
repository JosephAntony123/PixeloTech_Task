from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mobile', 'name', 'otp', 'is_verified']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.name = validated_data.get('name', instance.name)
        instance.otp = validated_data.get('otp', instance.otp)
        instance.is_verified = validated_data.get(
            'is_verified', instance.is_verified)
        instance.save()
        return instance
