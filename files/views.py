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
from folders.serializers import FolderSerializer


# Create your views here.
class File(APIView):
  permission_classes = (permissions.IsAuthenticated,)

  def get(self, request, id, format=None):
    user = self.request.user

    # file_id, user
    try:
      f = FileModel.objects.filter(id=id, owner=user.id).first()
      if f is None:
        return Response({'error': False, 'message': f'file {id} not found', 'data': None}, status=400)
      file_ser = FileSerializer(f)
      return Response({'error': False, 'data': file_ser.data})
    except Exception as e:
      print(e)
      print('cannot get file')
      return Response({'error': True, 'message': 'cannot get file', 'details': e, 'data': None})


  def delete(self, request, id, format=None):
    try:
      f = FileModel.objects.filter(id=id, owner=user.id).first()
      if f is None:
        return Response({'error': True, 'message': f'file {id} not found', 'data': None}, status=400)
      f_id = f.id
      f.delete()
      f_ser = FileSerializer(f)
      f_temp = f_ser.data
      f_temp['id'] = f_id
      return Response({'error': False, 'message': 'file deleted', 'data': f_temp})
    except Exception as e:
      print(e)
      return Response({'error': True, 'message': 'file cannot be deleted', 'details': e})


  # for now we only update the filename
  def put(self, request, id, format=None):
    file_name = request.data.get('fileName')

    if file_name is None: # add additional file name validations
      return Response({'error': True, 'message': 'missing \'fileName\' from request body'}, status=400)

    try:
      f = FileModel.objects.filter(id=id, owner=user.id).first()
      if f is None:
        return Response({'error': True, 'message': f'file {id} not found', 'data': None}, status=400)

      f.name = file_name # update here
      f.save()
      f_ser = FileSerializer(f)
      return Response({'error': False, 'message': 'file updated', 'data': f_ser.data})
    except Exception as e:
      print(e)
      return Response({'error': True, 'message': 'file cannot be updated', 'details': e})


class Files(APIView):
  permission_classes = (permissions.IsAuthenticated,)

  def get(self, request, format=None):
    user = self.request.user
    user = User.objects.get(id=user.id)

    # get all Folders from user
    folders = Folder.objects.all().filter(owner=user.id)
    folders = FolderSerializer(folders, many=True)
    folders = folders.data

    folders_data = []
    # get all files for all those folders
    for f in folders:
      files_in_folder = FileModel.objects.filter(parent_folder=f['id'], owner=user.id)
      files_in_folder = FileSerializer(files_in_folder, many=True)
      files_in_folder = files_in_folder.data
      folders_data.append({'folderName': f['name'], 'folderOwner': f['owner'], 'files': files_in_folder})

    return Response({'error': False, 'data': folders_data})

  def delete(self, request, format=None):
    pass


class CreateFile(APIView):
  permission_classes = (permissions.IsAuthenticated,)

  def post(self, request, format=None):
    user = self.request.user
    data = self.request.data

    file_name = data.get('fileName')
    parent_folder_id = data.get('parentFolderId')

    if file_name is None or parent_folder_id is None:
      return Response({'error': True, 'message': 'missing \'fileName\' or \'parentFolderId\' from request body'}, status=400)


    user = User.objects.get(id=user.id)
    folder = Folder.objects.filter(id=parent_folder_id, owner=user.id)
    try:
      f = FileModel.objects.create(name=file_name, parent_folder=folder.id, owner=user.id)
      f_ser = FileSerializer(f)
      return Response({'error': False, 'message': 'file created', 'data': f_ser.data})
    except Exception as e:
      print(e)
      print('cannot create file')
      return Response({'error': True, 'message': 'file cannot be created', 'details': e})