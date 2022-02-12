from django.urls import path
from .views import GetCSRFToken, LogInView, LogOutView, CheckAuthenticatedView, UserInfoView, UserTest


urlpatterns = [
  path('csrf_cookie', GetCSRFToken.as_view()),
  path('auth/login', LogInView.as_view()),
  path('auth/logout', LogOutView.as_view()),
  path('auth/loggedIn', CheckAuthenticatedView.as_view()),
  path('testing', UserTest.as_view()),
  path('profile', UserInfoView.as_view()),
]