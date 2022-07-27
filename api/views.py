from re import I
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """tests the api view"""

    def get(self, resquest, format=None):
        an_api = [
            'Loading.........',
            'Establishing Connection..............',
            'Successful!'
        ]

        return Response({'message': an_api, 'status': 'ok'})