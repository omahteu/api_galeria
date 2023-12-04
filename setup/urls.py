# mydrfproject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('amigos.urls')),
    path('api/', include('fila.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
