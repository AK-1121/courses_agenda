from rest_framework import serializers

from . import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id', 'title', 'description', 'lectors')


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Class
        fields = ('dt', 'duration', 'theme', 'plan', 'special_notes', 'course')


class LectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lector


