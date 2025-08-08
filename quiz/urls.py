from django.urls import path
from .views import register_view, quiz_list,  quiz_detail, submit_quiz, quiz_history

urlpatterns = [
    path('', quiz_list, name='quiz_list'),
    path('register/', register_view, name='register'),
    path('quiz/<int:quiz_id>/', quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/submit/', submit_quiz, name='submit_quiz'),
    path('history/', quiz_history, name='quiz_history'),


]
