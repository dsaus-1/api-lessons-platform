import requests
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from education.models import Course
from finance.models import Payment
from finance.serializers.payment_course import PaymentCourseSerializer
from finance.serializers.payment_lesson import PaymentLessonSerializer


class PaymentCourseListView(generics.ListAPIView):
    serializer_class = PaymentCourseSerializer
    queryset = Payment.objects.exclude(payment_course=None)

class PaymentLessonListView(generics.ListAPIView):
    serializer_class = PaymentLessonSerializer
    queryset = Payment.objects.exclude(payment_lesson=None)


class PaymentCourseAPIView(APIView):

    def get(self, *args, **kwargs):
        course_pk = self.kwargs.get('pk')
        course = get_object_or_404(Course, pk=course_pk)
        user = self.request.user

        payment_obj = Payment.objects.create(payment_sum=course.price, payment_method=Payment.METHOD_TRANSFER,
                                             payment_course=course, user=user)

        data = {
            "TerminalKey": settings.TERMINAL_KEY,
            "Amount": course.price,
            "OrderId": payment_obj.pk,
            "DATA": {
                "Email": user.email
            },
            "Receipt": {
                "Email": user.email,
                "Taxation": "osn",
                "Items": [
                    {
                        "Name": course.title,
                        "Price": course.price,
                        "Quantity": 1.00,
                        "Amount": course.price,
                        "PaymentObject": "commodity",
                        "Tax": "vat20"
                    }
                ]
            }
        }

        request = requests.post('https://securepay.tinkoff.ru/v2/Init/', json=data)

        if request.json()["Success"] == True:
            payment_obj.payment_url = request.json()["PaymentURL"]
            payment_obj.save()

        return Response({"url":request.json()["PaymentURL"], "data": request.json()})


