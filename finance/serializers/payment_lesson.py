from rest_framework import serializers

from finance.models import Payment


class PaymentLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'user',
            'payment_lesson',
            'date_payment',
            'payment_sum',
            'payment_method'
        )