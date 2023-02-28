from rest_framework import generics, status
from rest_framework.response import Response


from education.models import Course
from education.permissions import SuperPerms
from subscribe.models import Subscribe
from subscribe.permissions import OwnerSubscribePerm
from subscribe.serializers import SubscribeSerializer
from users.models import User


class SubscribeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()

    def post(self, request, *args, **kwargs):
        """Проверка данных на уникальность и создание экземпляра если данные уникальны"""
        data_student = User.objects.filter(email=request.data['student']).first().pk
        data_course = Course.objects.filter(title=request.data['course']).first().pk
        obj = self.queryset.filter(student=data_student).filter(course=data_course)
        if not obj:
            return self.create(request, *args, **kwargs)
        return Response(request.data, status=status.HTTP_200_OK)



class SubscribeDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [OwnerSubscribePerm | SuperPerms]

