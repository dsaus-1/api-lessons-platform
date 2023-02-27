from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from education.models import Course
from subscribe.models import Subscribe
from users.models import User


class SubscribeSerializer(serializers.ModelSerializer):
    student = SlugRelatedField(slug_field="email", queryset=User.objects.all())
    course = SlugRelatedField(slug_field="title", queryset=Course.objects.all())

    class Meta:
        model = Subscribe
        fields = ('student', 'course')