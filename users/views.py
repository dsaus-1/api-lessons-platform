from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.user.is_superuser:
    #         return queryset
    #
    # def list(self, request, *args, **kwargs):
    #     serializer_class =
    #     response = super().list(request, *args, **kwargs)
    #
    #

