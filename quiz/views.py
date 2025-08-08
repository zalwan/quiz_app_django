from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Quiz


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quiz_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})


def start_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'start_quiz.html', {'quiz': quiz, 'questions': questions})
