from datetime import datetime

import pytz
from rest_framework import viewsets, generics

from config import settings
from education.models import Course, Lesson
from education.permissions import ModeratorPerms, SuperPerms, OwnerCoursePerm, OwnerLessonPerm
from education.serializers import CourseSerializer, LessonSerializer
from education.tasks import check_course_update


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [SuperPerms | ModeratorPerms | OwnerCoursePerm]

    def perform_create(self, serializer):
        """ Переопределяем, чтобы сохранился owner_lesson"""
        return serializer.save(owner_course=self.request.user, time_update=datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE)))

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perms(['education.change_course', 'education.view_course']):
            return queryset
        return queryset.filter(owner_course=self.request.user)

    def perform_update(self, serializer):
        self.object = serializer.save()
        check_course_update.delay(self.object.pk)


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [ModeratorPerms | OwnerLessonPerm]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perms(['education.view_lesson', 'education.change_lesson']):
            return queryset
        return queryset.filter(owner_lesson=self.request.user)

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [SuperPerms]

    def perform_create(self, serializer):
        """ Переопределяем, чтобы сохранился owner_lesson"""
        return serializer.save(owner_lesson=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [OwnerLessonPerm | ModeratorPerms | SuperPerms]
    queryset = Lesson.objects.all()

    def perform_update(self, serializer):
        self.object = serializer.save()
        check_course_update.delay(self.object.pk)








