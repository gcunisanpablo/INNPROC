from django.urls import path
from documentacion import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("documentos/", views.documentos, name="documentos"),
    # todos los documentos
    path("buscar-documentos/", views.buscar_documentos, name="buscar_documentos"),
    path(
        "ver-pdf/<int:id>/<str:model_name>/<str:image_form>/<str:formatos_form>/",
        views.ver_pdf,
        name="ver_pdf",
    ),
    path("ver-pdf-solo/<int:id>/", views.ver_pdf_solo, name="ver_pdf_solo"),
    path(
        "ver-pdf-solo-formatos/<int:id>/",
        views.ver_pdf_solo_formatos,
        name="ver_pdf_solo_formatos",
    ),
    path("descargar/<str:file_name>/", views.download_generic, name="download_generic"),
    path(
        "download-documents/<int:document_id>/",
        views.download_documents,
        name="download_documents",
    ),
    path(
        "download-format/<int:document_id>/",
        views.download_format,
        name="download_format",
    ),
    path(
        "eliminar-imagen/<int:image_id>/<str:model_name>/<str:model_name_base>/<str:formatos_form>/",
        views.delete_image,
        name="eliminar_imagen",
    ),
    path(
        "delete-format/<int:format_id>/<str:model_name>/<str:model_name_base>/<str:image_form>/",
        views.delete_format,
        name="delete_format",
    ),  # Añade esta línea
    path("download-file/<int:document_id>/", views.download_file, name="download_file"),
    path("download-pdf/<int:id>/", views.download_pdf_visualizar, name="download_pdf"),
    path(
        "download-pdf-format/<int:id>/",
        views.download_pdf_visualizar_solo_formato,
        name="download_pdf_visualizar_solo_formato",
    ),
    # Descargar
    path("documents/<int:pk>/download/", views.download, name="download"),
    # politica de calidad
    path("politica-calidad/", views.politica_calidad, name="politica-calidad"),
    path("politica-calidad/politica/", views.politica, name="politica"),
    path("politica-calidad/objetivos/", views.objetivos, name="objetivos"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
