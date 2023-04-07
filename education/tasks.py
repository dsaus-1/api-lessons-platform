from datetime import datetime, timedelta

import pytz
from celery import shared_task
from django.core.mail import send_mail

from config import settings
from education.models import Course
from subscribe.models import Subscribe


@shared_task
def check_course_update(course_pk):
    subscribers = Subscribe.objects.filter(course=course_pk)
    course = Course.objects.filter(pk=course_pk).first()
    time = datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE)) - timedelta(hours=4)

    if time >= course.time_update:

        for student in subscribers:
            send_mail(subject='Обновления курса',
                      message=f'Смотрите обновления курса "{course.title}" по ссылке {settings.BASE_URL}course/{course_pk}',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[student.student.email],
                      fail_silently=False)

    course.time_update = datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE))
    course.save()


@shared_task
def check_lesson_update(lesson_pk):
    courses = Course.objects.filter(lessons=lesson_pk)
    time = datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE)) - timedelta(hours=4)

    for course in courses:
        if time >= course.time_update:
            subscribers = Subscribe.objects.filter(course=course.pk)
            for student in subscribers:
                send_mail(subject='Обновления курса',
                          message=f'Смотрите обновления курса "{course.title}" по ссылке {settings.BASE_URL}course/{course.pk}',
                          from_email=settings.EMAIL_HOST_USER,
                          recipient_list=[student.student.email],
                          fail_silently=False)

        course.time_update = datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE))
        course.save()



