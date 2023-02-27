from django.db import models

from education.models import Course
from users.models import User


class Subscribe(models.Model):

    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Студент')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
