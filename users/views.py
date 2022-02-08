from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .models import User
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import auth
from .serializers import UserSerializer

# https://www.youtube.com/watch?v=NFHiT4ncPD8

@method_decorator(csrf_exempt, name='dispatch')
class CheckAuthenticatedView(APIView):
  def get(self, request, format=None):
    isAuthenticated = User.is_authenticated

    if isAuthenticated:
      return Response({'error': False, 'message': {'authenticated': True}})
    else:
      return Response({'error': False, 'message': {'authenticated': False}})


@method_decorator(csrf_exempt, name='dispatch')
class LogInView(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request, format=None):
    data = self.request.data

    missing = []
    if 'username' not in data:
      missing.append('username')
    if 'password' not in data:
      missing.append('password')
        
    if len(missing) > 0:
      return Response({'error': True, 'message': ", ".join(missing) + " missing in json body"})
    
    username = data['username']
    password = data['password']

    user = auth.authenticate(username=username, password=password)

    if user is None:
      return Response({'error': True, 'message': 'username or password is incorrect'}, status=400)
    else:
      auth.login(request, user)
      return Response({'error': False, 'message': 'login success', 'data': {'username': username}})


@method_decorator(csrf_exempt, name='dispatch')
class LogOutView(APIView):
  def post(self, request, format=None):
    try:
      auth.logout(request)
      return Response({'error': False, 'message': 'user logged out'})
    except:
      return Response({'error': True, 'message': 'user could not be logged out'})


@method_decorator(csrf_exempt, name='dispatch')
class UserInfoView(APIView):
  # permission_classes = (permissions.IsAuthenticated,)


  def get(self, request, format=None):
    user = self.request.user

    print(user)

    user = User.objects.get(id=user.id)

    user_info = UserSerializer(user)

    return Response({'error': False, 'data': user_info.data})



@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
  permission_classes = (permissions.AllowAny,)

  def get(self, request, format=None):
    return Response({'error': False, 'message': 'CSRF cookie set'})