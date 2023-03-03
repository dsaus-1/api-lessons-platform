from django.db import models

from education.models import Course, Lesson
from users.models import User


NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):
    METHODS = (
        ('cash', 'наличные'),
        ('money transfer', 'перевод на счет'),
    )
    METHOD_CASH = 'cash'
    METHOD_TRANSFER = 'money transfer'

    STATUS = (
        ('created', 'создан'),
        ('confirmed', 'подтвержден')
    )

    CREATED = 'created'
    CONFIRMED = 'confirmed'

    date_payment = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    payment_sum = models.FloatField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=30, choices=METHODS, verbose_name='способ оплаты')
    status = models.CharField(max_length=20, default=CREATED, choices=STATUS, verbose_name='Статус оплаты')
    url = models.URLField(verbose_name='Ссылка на оплату', **NULLABLE)

    payment_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'{self.user.email} {self.payment_sum}'
