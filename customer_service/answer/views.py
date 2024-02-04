import openai
from django.shortcuts import render
from decouple import config
from .models import Question, Answer

openai.api_key = config('OPENAI_API_KEY')

# Create your views here.

def generate_answer(question_content):
    # Utiliza gpt-3.5-turbo en lugar de engine
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question_content}
        ],
        max_tokens=500
    )

    answer_content = response.choices[0].message.content

    return answer_content

def answer_question(request):
    try:
        question_content = request.session.get('question_content')
        question = Question.objects.filter(content__iexact=question_content).first()
        if not question:
            new_question = Question(content=question_content)
            new_question.save()

        if question:
            answer = Answer.objects.filter(question=question).first()
            context = {'question': question, 'answer': answer}
            return render(request, 'answer.html', context)

        else:
            latest_question = Question.objects.latest('timestamp')
            question_content = latest_question.content
            answer_content = generate_answer(question_content)

            answer = Answer(content=answer_content)
            answer.question = latest_question
            answer.save()

            return render(request, 'answer.html', {'question': latest_question, 'answer': answer})
    except Question.DoesNotExist:
        return render(request, 'no_questions.html')