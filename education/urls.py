from django.urls import path
from rest_framework.routers import DefaultRouter
from education.apps import EducationConfig
from education.views import CourseViewSet, LessonListView, LessonCreateAPIView, LessonUpdateAPIView

app_name = EducationConfig.name
router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [
    path('lesson/list/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    ] + router.urls