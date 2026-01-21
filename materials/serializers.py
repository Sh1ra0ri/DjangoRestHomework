from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True, source="lesson_set")
    number_of_lessons = serializers.SerializerMethodField()

    def get_number_of_lessons(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = "__all__"
