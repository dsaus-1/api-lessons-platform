from rest_framework import viewsets

from users.models import User
from users.permissions import OwnerProfile
from users.serializers import UserSerializer, AllUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [OwnerProfile]

    def get_serializer_class(self):
        if self.action == 'create' and 'update':
            return UserSerializer
        return AllUserSerializer

