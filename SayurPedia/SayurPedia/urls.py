
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search_sayur/', include('search_sayur.urls')),
    path('data_semua_sayur/', include('data_semua_sayur.urls')),
    path('', views.index),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
