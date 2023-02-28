from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from users.models import User
from users.permissions import OwnerProfile
from users.serializers import UserSerializer, AllUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' and 'update':
            return UserSerializer
        return AllUserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [OwnerProfile()]

