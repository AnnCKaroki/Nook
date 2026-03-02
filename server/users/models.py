from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Grade(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(AbstractUser):

    TEACHER = 'teacher'
    STUDENT = 'student'
    ROLE_CHOICES = [(TEACHER, 'Teacher'), (STUDENT, 'Student')]

    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES )

    def __str__(self):
        return self.username
