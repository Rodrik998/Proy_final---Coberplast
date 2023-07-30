from django.urls import path
from products.views import Create_product

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('catalogue/', Create_product, name='Catalogo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
