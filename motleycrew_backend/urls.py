from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include('users.urls')),
  path('api/', include('files.urls')),
  path('api/', include('folders.urls')),
  path('api/', include('route_slips.urls')),
]
