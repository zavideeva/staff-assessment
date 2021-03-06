from django.contrib.auth.models import User

from rest_framework import serializers

from .models import FeedbackCourse, FeedbackProf, FeedbackTA, Course


class FeedbackCoursePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackCourse
        fields = '__all__'


class FeedbackCourseGetSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )

    class Meta:
        model = FeedbackCourse
        fields = '__all__'


class CourseGetSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )

    class Meta:
        model = Course
        fields = '__all__'


class CoursePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class FeedbackProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackProf
        fields = '__all__'


class FeedbackTASerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackTA
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'courses')


class StudentSerializer(serializers.ModelSerializer):
    student_courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'student_courses')


class TASerializer(serializers.ModelSerializer):
    ta_courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'ta_courses')
