from rest_framework import generics

from finance.models import Payment
from finance.serializers.payment_course import PaymentCourseSerializer
from finance.serializers.payment_lesson import PaymentLessonSerializer


class PaymentCourseListView(generics.ListAPIView):
    serializer_class = PaymentCourseSerializer
    queryset = Payment.objects.exclude(payment_course=None)

class PaymentLessonListView(generics.ListAPIView):
    serializer_class = PaymentLessonSerializer
    queryset = Payment.objects.exclude(payment_lesson=None)
