from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # app usuarios
    path("", include("usuarios.urls")),
    # app mapa procesos
    path("", include("mapa_procesos.urls")),
    # app documentacion
    path("", include("documentacion.urls")),
    # gestor de archivos
    path("", include("gestor_archivos.urls")),
    # app glosario
    path("", include("glosario.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
