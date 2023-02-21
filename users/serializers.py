from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from finance.models import Payment
from users.models import User

class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payment = PaymentUserSerializer(many=True, source='payment_set', read_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'phone',
            'city',
            'avatar',
            'password',
            'payment'
        )

