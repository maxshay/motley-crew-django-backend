from django.urls import path
from .views import GetCSRFToken, LogInView, UserInfoView

from rest_framework_simplejwt.views import (
  TokenRefreshView,
  TokenVerifyView
)
# urlpatterns = [
#   path('profile', UserInfoView.as_view()),
#   path('csrf_cookie', GetCSRFToken.as_view()),
#   path('auth/login', LogInView.as_view()),
#   path('auth/logout', LogOutView.as_view()),
#   path('auth/loggedin', CheckAuthenticatedView.as_view()),
# ]


urlpatterns = [
  path('profile', UserInfoView.as_view()),
  path('csrf_cookie', GetCSRFToken.as_view()),
  path('auth/login', LogInView.as_view()),
  path('auth/token/verify', TokenVerifyView.as_view(), name='token_verify'),
  path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
  # path('auth/logout', LogOutView.as_view()),
  # path('auth/loggedin', CheckAuthenticatedView.as_view()),
]