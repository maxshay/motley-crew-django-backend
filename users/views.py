from django.contrib import auth
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.views import TokenObtainPairView

# for search
from django.contrib.postgres.search import TrigramWordSimilarity
from django.db.models import Value as V
from django.db.models.functions import Concat

# serializer
from .serializers import UserSerializer, LogInSerializer

# models
from .models import User as UserModel
from django.views.decorators.csrf import ensure_csrf_cookie


class LogInView(TokenObtainPairView): # new
  serializer_class = LogInSerializer


class UserSearch(APIView):
  def get(self, request, format=None):
    query_string = self.request.query_params.get('query', None)
    if query_string is None or query_string == "":
      return Response({'query': ['must be non empty string']}, status=400)

    users_data = UserModel.objects.annotate(
      full_name=Concat('first_name', V(' '), 'last_name'),
      similarity=TrigramWordSimilarity(query_string, 'full_name' ),
    ).filter(similarity__gt=0.5).order_by('-similarity')
    users_ser = UserSerializer(users_data, many=True)
    # print(users_ser.data)
    return Response({'users': users_ser.data})


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