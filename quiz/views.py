from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Quiz, Question, Answer, QuizResult
from django.contrib.auth.decorators import login_required


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


@login_required
def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'quiz_detail.html', {'quiz': quiz, 'questions': questions})


@login_required
def submit_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    total = questions.count()
    correct = 0

    for question in questions:
        selected = request.POST.get(str(question.id))
        if selected:
            answer = Answer.objects.get(id=int(selected))
            if answer.is_correct:
                correct += 1

    score = int((correct / total) * 100)

    QuizResult.objects.create(
        user=request.user,
        quiz=quiz,
        score=score
    )

    return render(request, 'quiz_result.html', {
        'quiz': quiz,
        'score': score,
        'correct': correct,
        'total': total,
    })


def quiz_history(request):
    results = QuizResult.objects.filter(
        user=request.user).order_by('-submitted_at')
    return render(request, 'quiz_history.html', {'results': results})
