from django.contrib import admin
from django.urls import path

from django_base.views import index

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name = 'inicio'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
