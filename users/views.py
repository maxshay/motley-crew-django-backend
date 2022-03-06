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


class User(generics.RetrieveAPIView):
  serializer_class = UserSerializer
  lookup_field = 'id'

  def get_queryset(self):
    user = self.request.user
    return UserModel.objects.filter(id=user.id)



@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
  permission_classes = (permissions.AllowAny,)

  def get(self, request, format=None):
    return Response({'error': False, 'message': 'CSRF cookie set', 'data': None})