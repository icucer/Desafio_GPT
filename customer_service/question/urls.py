from django.urls import path
from .views import create_question

urlpatterns = [
    path('question/', create_question, name='create_question'),
]