from django.contrib import admin

from finance.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('date_payment', 'payment_sum', 'payment_method', 'payment_course', 'payment_lesson', 'user',)
