from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializes a user name field for testing our API view"""

    name = serializers.CharField(max_length=10)