from django.urls import path
from .views import register_view, quiz_list_view

urlpatterns = [
    path('', quiz_list_view, name='quiz_list'),
    path('register/', register_view, name='register'),
]
