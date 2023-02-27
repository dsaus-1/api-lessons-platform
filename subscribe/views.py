from rest_framework import generics
from rest_framework.generics import get_object_or_404

from education.permissions import SuperPerms
from subscribe.models import Subscribe
from subscribe.permissions import OwnerSubscribePerm
from subscribe.serializers import SubscribeSerializer


class SubscribeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()

class SubscribeDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [SuperPerms | OwnerSubscribePerm]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)

        return obj
