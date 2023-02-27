from rest_framework import serializers

from education.models import Course, Lesson
from education.validators import VideoValidator
from subscribe.models import Subscribe


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = (
            'title',
            'preview',
            'description',
            'video_url',
            'owner_lesson'
        )
        validators = [VideoValidator(field='video_url')]


class CourseSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    subscription = serializers.SerializerMethodField()

    def get_subscription(self, course):
        user = self.context['request'].user.id

        obj = Subscribe.objects.filter(course=course.id).filter(student=user)
        if obj:
            return 'Subscribed'
        return 'Unsubscribed'


    def get_number_of_lessons(self, instance):
        return instance.lessons.count()

    class Meta:
        model = Course
        fields = (
            'title',
            'preview',
            'description',
            'students',
            'lessons',
            'number_of_lessons',
            'owner_course',
            'subscription'
        )


