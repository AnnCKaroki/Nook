from django.db import models
from users.models import User, Grade

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)

    teachers = models.ManyToManyField(User, related_name='teaching_subjects')

    students = models.ManyToManyField(User, related_name='learning_subjects')

    grade = models.ManyToManyField(Grade)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.name

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    pass_mark = models.IntegerField(default=70)

    def __str__(self):
        return self.name

class QuizAttempt(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_attempts')
    score = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    attempts_used = models.IntegerField(default=0)

    class Meta:
        unique_together = ('student', 'quiz')


    def __str__(self):
        return f"{self.student.username} - {self.quiz.name} - {self.score}"
