from rest_framework import serializers

from education.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            'title',
            'preview',
            'description',
            'students',
        )


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = (
            'title',
            'preview',
            'description',
            'video_url',
        )