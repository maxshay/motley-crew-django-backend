from django.urls import path
from .views import GetCSRFToken, LogInView, LogOutView, CheckAuthenticatedView, UserInfoView


urlpatterns = [
  path('profile', UserInfoView.as_view()),
  path('csrf_cookie', GetCSRFToken.as_view()),
  path('auth/login', LogInView.as_view()),
  path('auth/logout', LogOutView.as_view()),
  path('auth/loggedin', CheckAuthenticatedView.as_view()),
  # path('profile', UserInfoView.as_view()),
]