from rest_framework import viewsets, generics

from education.models import Course, Lesson
from education.permissions import ModeratorPerms, SuperPerms, OwnerCoursePerm, OwnerLessonPerm
from education.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [SuperPerms | ModeratorPerms | OwnerCoursePerm]

    def create(self, request, *args, **kwargs):
        request.data['owner_course'] = request.user.pk
        answer = super().create(request, *args, **kwargs)
        return answer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perms(['education.change_course', 'education.view_course']):
            return queryset
        return queryset.filter(owner_course=self.request.user)



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

    def create(self, request, *args, **kwargs):
        request.data['owner_lesson'] = request.user.pk
        answer = super().create(request, *args, **kwargs)
        return answer

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [OwnerLessonPerm | ModeratorPerms | SuperPerms]
    queryset = Lesson.objects.all()







