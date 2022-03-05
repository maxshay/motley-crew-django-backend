from django.contrib import auth
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from .serializers import UserSerializer, LogInSerializer
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import User

# new
from rest_framework_simplejwt.views import TokenObtainPairView


class LogInView(TokenObtainPairView): # new
  serializer_class = LogInSerializer


class User(APIView):
  def get(self, request, format=None):
    user = request.user
    user = User.objects.get(id=user.id)
    user_info = UserSerializer(user)

    return Response({'error': False, 'message': 'ok', 'data': user_info.data})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
  permission_classes = (permissions.AllowAny,)

  def get(self, request, format=None):
    return Response({'error': False, 'message': 'CSRF cookie set', 'data': None})