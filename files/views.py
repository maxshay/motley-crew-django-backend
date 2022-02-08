from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
import json


from .serializers import FileSerializer
from .models import File as FileModel
from users.models import User
from folders.models import Folder


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class File(APIView):
  permission_classes = (permissions.IsAuthenticated,)

  def get():

    # file_id, user


    
    # get all files for all those folders

    return Response({'error': False, 'message': 'ok', 'data': {}})




@method_decorator(csrf_exempt, name='dispatch')
class Files(APIView):
  permission_classes = (permissions.IsAuthenticated,)

  def get():

    # get all Folders from user

    # get all files for all those folders

    return Response({'error': False, 'message': 'ok', 'data': {}})
