from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    special_notes = models.TextField()


class Class(models.Model):
    dt = models.DateTimeField()
    duration = models.IntegerField(default=90)
    theme = models.CharField(max_length=1024)
    plan = models.TextField()
    special_notes = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Lector(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contacts = models.CharField(max_length=2048)
    personal_info = models.CharField(max_length=2048)
    courses = models.ManyToManyField(Course, related_name='lectors', blank=True)


