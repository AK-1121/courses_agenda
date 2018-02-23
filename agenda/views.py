from django.shortcuts import render

from rest_framework import viewsets

from . import models
from . import serializers


class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = models.Class
    serializer_class = serializers.ClassSerializer


class LectorViewSet(viewsets.ModelViewSet):
    queryset = models.Lector
    serializer_class = serializers.LectorSerialize
