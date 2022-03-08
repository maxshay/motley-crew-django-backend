from django.http import Http404
from rest_framework.views import APIView
from rest_framework import permissions, generics
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from motleycrew_backend.permissions import IsOwner
import json

# models
from .models import File as FileModel
from users.models import User
from folders.models import Folder as FolderModel

# serializers
from .serializers import FileSerializer, CreateFileSerializer, FilesSerializer
from folders.serializers import FolderSerializer


# think of these as controllers
# Create your views here.
class File(generics.RetrieveDestroyAPIView):
  permission_classes = (IsOwner,)
  queryset = FileModel.objects.all()
  serializer_class = FileSerializer
  lookup_field = 'id'


"""
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
"""

class Files(generics.ListAPIView):
  serializer_class = FilesSerializer

  def get_queryset(self):
    user = self.request.user
    return FolderModel.objects.filter(owner=user)



"""
class Files(APIView):
  permission_classes = (permissions.IsAuthenticated,)

  def get(self, request, format=None):
    user = self.request.user
    user = User.objects.get(id=user.id)

    # get all Folders from user
    folders = FolderModel.objects.all().filter(owner=user.id)
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
"""

class CreateFile(generics.CreateAPIView):
  permission_classes = (IsOwner,)
  serializer_class = CreateFileSerializer
  queryset = FolderModel.objects.all()
  # lookup_field = 'id'

  # def get_serializer_context(self):
  #   context = super().get_serializer_context()
  #   context.update({'test': 'testing123'})
  #   return context
  def get_object(self):
    try:

      folder = FolderModel.objects.get(pk=self.kwargs.get('id'))
    except FolderModel.DoesNotExist as e:
      raise Http404
    self.check_object_permissions(self.request, folder)
    return folder

  def perform_create(self, serializer):
    parent_folder = self.get_object()
    serializer.save(parent_folder=parent_folder)


  """
  def post(self, request, format=None):
    user = self.request.user
    data = self.request.data
    # file_data = self.request.files

    # TODO: get file from request
    file_name = data.get('fileName')
    parent_folder_id = data.get('parentFolderId')

    if file_name is None or parent_folder_id is None:
      return Response({'error': True, 'message': 'missing \'fileName\' or \'parentFolderId\' from request body'}, status=400)

    # file_data = self.request.files
    # print(file_data)

    user = User.objects.get(id=user.id)
    folder = Folder.objects.filter(id=parent_folder_id, owner=user.id)
    try:
      f = FileModel.objects.create(name=file_name, parent_folder=folder.id, owner=user.id, file=file)
      f_ser = FileSerializer(f)
      return Response({'error': False, 'message': 'file created', 'data': f_ser.data})
    except Exception as e:
      print(e)
      print('cannot create file')
      return Response({'error': True, 'message': 'file cannot be created', 'details': e})
  """