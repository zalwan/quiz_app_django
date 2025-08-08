from django.urls import path
from .views import register_view, quiz_list, start_quiz

urlpatterns = [
    path('', quiz_list, name='quiz_list'),
    path('register/', register_view, name='register'),
    path('quiz/<int:quiz_id>/start/', start_quiz, name='start_quiz'),

]
