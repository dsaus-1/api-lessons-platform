from rest_framework import serializers

from finance.models import Payment


class PaymentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'user',
            'payment_course',
            'date_payment',
            'payment_sum',
            'payment_method'
        )