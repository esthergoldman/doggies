from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('', include('accounts.urls')),
    path('', include('adopt.urls')),
    path('', include('contacts.urls')),
    path('', include('events.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
