from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_youtube_link


class LessonSerializer(serializers.ModelSerializer):
    link = serializers.URLField(
        validators=[validate_youtube_link], required=False, allow_blank=True
    )

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True, source="lesson_set")
    number_of_lessons = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    def get_number_of_lessons(self, obj):
        return obj.lesson_set.count()

    def get_is_subscribed(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = "__all__"
