from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='аватар', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    students = models.ManyToManyField(User, verbose_name='ученики', **NULLABLE)
    lessons = models.ManyToManyField('Lesson', verbose_name='уроки', **NULLABLE)
    owner_course = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE, related_name='owner_course_get')

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='lesson/', verbose_name='аватар', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    video_url = models.URLField(verbose_name='ссылка на видео')

    students = models.ManyToManyField(User, verbose_name='ученики', **NULLABLE)
    owner_lesson = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE, related_name='owner_lesson_get')

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    def __str__(self):
        return self.title


