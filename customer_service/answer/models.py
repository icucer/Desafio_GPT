from django.db import models
from question.models import Question

# Create your models here.

class Answer(models.Model):
    content = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    timestamp = models.DateTimeField(auto_now_add=True)