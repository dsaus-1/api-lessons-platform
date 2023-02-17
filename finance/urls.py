from django.urls import path

from finance.apps import FinanceConfig
from finance.views import PaymentCourseListView, PaymentLessonListView

app_name = FinanceConfig.name


urlpatterns = [
    path('course/list/', PaymentCourseListView.as_view(), name='course_list'),
    path('lesson/list/', PaymentLessonListView.as_view(), name='lesson_list')
    ]