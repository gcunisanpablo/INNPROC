from django.urls import path
from gestor_archivos import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # especifico
    path(
        "buscar-documentos-especificos/<str:model_name>/",
        views.lista_documentos_especificos,
        name="lista_documentos_especificos",
    ),
    path(
        "buscar-requisitos-legales-normativos-epecificos/<str:model_name>/",
        views.lista_requisitos_legales_normativos_epecificos,
        name="lista_requisitos_legales_normativos_epecificos",
    ),
    path(
        "buscar-requisitos-necesidades-partes-interesadas-epecificos/<str:model_name>/",
        views.lista_requisitos_necesidades_partes_interesadas_epecificos,
        name="lista_requisitos_necesidades_partes_interesadas_epecificos",
    ),
    path(
        "buscar-indicadores-especificos/<str:model_name>/",
        views.lista_indicadores_especificos,
        name="lista_indicadores_especificos",
    ),
    path("guardar-caracterizacion/", views.save_html, name="guardar-caracterizacion"),
    path(
        "crear-documento/<str:model_name>/<str:form_name>/",
        lambda request, model_name, form_name: views.crear_documento(
            request, model_name, form_name
        ),
        name="crear_documento",
    ),
    path(
        "eliminar-documento/<str:model_name>/<int:id>/",
        views.eliminar_documento,
        name="eliminar_documento",
    ),
    path(
        "subir-diagrama-procedimientos/<str:model_name>/<str:form_name>/",
        views.cargar_imagen,
        name="cargar_imagen",
    ),  # URL para cargar la imagen
    path(
        "lista-diagramas-procedimientos/<str:model_name>/",
        views.lista_img,
        name="lista_img",
    ),
    path(
        "ver-diagrama-procedimientos/<str:model_name>/<int:img_id>/",
        views.detalle_img,
        name="detalle_img",
    ),
    path(
        "eliminar-diagrama-procedimientos/<str:model_name>/<int:id>/",
        views.eliminar_imagen,
        name="eliminar_imagen",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
