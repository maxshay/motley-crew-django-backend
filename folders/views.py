from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
import json

from .serializers import FolderSerializer
from .models import Folder
from users.models import User

# dev
import logging

@method_decorator(csrf_exempt, name='dispatch')
class GetAllFolders(APIView):
  permission_classes = (permissions.IsAuthenticated,)
    
  def get(self, request, format=None):
    user = self.request.user
    user = User.objects.get(id=user.id)

    folders = Folder.objects.all().filter(user=user) # all
    folder_info = FolderSerializer(folders, many=True)
    return Response({'error': False, 'data': folder_info.data})


@method_decorator(csrf_exempt, name='dispatch')
class CreateFolder(APIView):
  permission_classes = (permissions.IsAuthenticated,)

  def post(self, request, format=None):
    user = self.request.user
    data = self.request.data
    folder_name = data.get('folderName')

    if folder_name is None:
      return Response({'error': True, 'message': 'missing \'folderName\' from request body'}, status=400)


    user = User.objects.get(id=user.id)
    try:
      f = Folder.objects.create(name=folder_name, user=user)
      f_ser = FolderSerializer(f)
      return Response({'error': False, 'message': 'folder created', 'data': f_ser.data})
    except Exception as e:
      print(e)
      print('cannot create folder')
      return Response({'error': True, 'message': 'folder cannot be created', 'details': e})

