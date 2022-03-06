from django.contrib import auth
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.views import TokenObtainPairView

# serializer
from .serializers import UserSerializer, LogInSerializer

# models
from .models import User as UserModel
from django.views.decorators.csrf import ensure_csrf_cookie



class LogInView(TokenObtainPairView): # new
  serializer_class = LogInSerializer


class User(generics.RetrieveUpdateAPIView):
  serializer_class = UserSerializer
  lookup_field = 'id'

  def get_object(self):
    user = self.request.user
    user = UserModel.objects.get(id=user.id)
    return user


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
  permission_classes = (permissions.AllowAny,)

  def get(self, request, format=None):
    return Response({'error': False, 'message': 'CSRF cookie set', 'data': None})