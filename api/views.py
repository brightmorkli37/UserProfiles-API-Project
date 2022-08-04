from api import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from api import permissions
from api.serializers import UserProfileSerializer
from api.models import UserProfile


class UserProfileViewSet(viewsets.ModelViewSet):    
    """Handles creating and Updating Profiles"""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


