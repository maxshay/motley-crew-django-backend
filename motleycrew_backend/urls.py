from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include('users.urls')),
  path('api/', include('files.urls')),
  path('api/', include('folders.urls')),
  path('api/', include('route_slips.urls')),
  path('api/', include('route_items.urls')),
  path('api/', include('messages.urls')),
]

def get_urls():
  return [f'{a.pattern}{p.pattern}' for a in urlpatterns[1:] for p in a.url_patterns]