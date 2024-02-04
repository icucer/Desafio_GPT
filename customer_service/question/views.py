from django.shortcuts import render, redirect
from .models import Question

# Create your views here.

def create_question(request):
    if request.method == 'POST':
        question_content = request.POST.get('question_content', '')
        request.session['question_content'] = question_content
        return redirect('answer_question')
    
    return render(request, 'question.html')