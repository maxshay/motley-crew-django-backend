from django.urls import path
from .views import Message, Messages, ReadMessage


urlpatterns = [
  path('message/<str:id>', Message.as_view()),
  path('message/<str:id>/mark-read', ReadMessage.as_view()),
  path('messages', Messages.as_view()),
]