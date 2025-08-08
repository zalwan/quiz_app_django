from django.urls import path
from .views import register_view, quiz_list

urlpatterns = [
    path('', quiz_list, name='quiz_list'),
    path('register/', register_view, name='register'),
]
