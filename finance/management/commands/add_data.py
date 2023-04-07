from django.core.management import BaseCommand

from education.models import Course, Lesson
from finance.models import Payment
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        finance_data = [
            {
                "payment_sum": 1200.0,
                "payment_method": Payment.METHOD_CASH,
                "payment_course": Course.objects.filter(pk=1).first(),
                "user": User.objects.filter(pk=1).first()
            },
            {
                "payment_sum": 1344.54,
                "payment_method": Payment.METHOD_TRANSFER,
                "payment_course": Course.objects.filter(pk=1).first(),
                "user": User.objects.filter(pk=1).first()
            },
            {
                "payment_sum": 1344.54,
                "payment_method": Payment.METHOD_TRANSFER,
                "payment_course": Course.objects.filter(pk=2).first(),
                "user": User.objects.filter(pk=2).first()
            },
            {
                "payment_sum": 344.05,
                "payment_method": Payment.METHOD_TRANSFER,
                "payment_lesson": Lesson.objects.filter(pk=2).first(),
                "user": User.objects.filter(pk=2).first()
            },
            {
                "payment_sum": 211.65,
                "payment_method": Payment.METHOD_TRANSFER,
                "payment_lesson": Lesson.objects.filter(pk=1).first(),
                "user": User.objects.filter(pk=2).first()
            },
            {
                "payment_sum": 211.65,
                "payment_method": Payment.METHOD_CASH,
                "payment_lesson": Lesson.objects.filter(pk=1).first(),
                "user": User.objects.filter(pk=1).first()
            },
        ]
        payment_list = []
        Payment.objects.all().delete()

        for data in finance_data:
            payment_list.append(Payment(**data))

        Payment.objects.bulk_create(payment_list)
