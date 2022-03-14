from django.urls import path
from .views import GetCSRFToken, LogInView, User, UserSearch

from rest_framework_simplejwt.views import (
  TokenRefreshView,
  TokenVerifyView
)

urlpatterns = [
  path('profile', User.as_view() ),
  path('user/search', UserSearch.as_view() ),
  path('csrf_cookie', GetCSRFToken.as_view()),
  path('auth/login', LogInView.as_view()),
  path('auth/token/verify', TokenVerifyView.as_view(), name='token_verify'),
  path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]