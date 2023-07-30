from django.contrib import admin
from django.urls import path, include

from django_base.views import index

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name = 'inicio'),
    path('admin/', admin.site.urls),

    path('products/', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
