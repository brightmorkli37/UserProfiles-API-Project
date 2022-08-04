from rest_framework import serializers
from api.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the UserProfile model.
    """
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'style': {'input_type': 'password'}
        }

    def create(self, validated_data):
        """
        Create a new user profile.
        """
        user =  UserProfile.objects.create(**validated_data)
        return user

    # def update(self, instance, validated_data):
    #     """
    #     Update a user profile.
    #     """
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.set_password(validated_data.get('password', instance.password))
    #     instance.save()
    #     return instance

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)