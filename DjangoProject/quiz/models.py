from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.question_text)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return str(self.choice_text)

class QuizMarks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date of attempt',default=datetime.now())
