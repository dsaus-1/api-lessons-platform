from rest_framework import serializers

from education.models import Course, Lesson

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = (
            'title',
            'preview',
            'description',
            'video_url',
        )


class CourseSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            'title',
            'preview',
            'description',
            'students',
            'lessons',
            'number_of_lessons'
        )

    def get_number_of_lessons(self, instance):
        return instance.lessons.count()


