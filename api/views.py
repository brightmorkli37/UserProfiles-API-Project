from re import I
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import *
from rest_framework import status



class HelloApiView(APIView):
    """tests the api view"""

    serializer_class = HelloSerializer

    def get(self, resquest, format=None):
        an_api = [
            'Loading.........',
            'Establishing Connection..............',
            'Successful!'
        ]

        return Response({'message': an_api, 'status': 'ok'})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})