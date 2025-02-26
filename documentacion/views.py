import os
from itertools import chain
import unicodedata
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.http import (
    Http404,
    JsonResponse,
    HttpResponse,
    FileResponse,
)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from gestor_archivos.models import Document
from .models import DocumentFormatosAsociados
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404, redirect, render
from django.apps import apps
from documentacion import forms
import subprocess
import os
import subprocess
import tempfile
import atexit
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.apps import apps
import os


# Funcion verificacion logeado custom
def login_required_custom(view_func):
    return login_required(view_func, login_url="login")


def normalize_and_uppercase(input_string):
    """Normaliza el texto eliminando tildes y convirtiendo a mayúsculas."""
    # Normalizar el texto para eliminar tildes y otros signos diacríticos, luego convertir a mayúsculas
    return (
        unicodedata.normalize("NFD", input_string)
        .encode("ascii", "ignore")
        .decode("ascii")
        .upper()
    )


# LISTA COMBINADA DOCUMENTOS Y FORMATOS y buscador
def documentos(request):
    # Obtener los documentos y formatos asociados
    documentos_list = Document.objects.all().order_by("id_archivo")
    formatos_list = DocumentFormatosAsociados.objects.all().order_by("id")

    # Combinar ambas listas
    combined_list = list(chain(documentos_list, formatos_list))

    query = request.GET.get(
        "q", ""
    ).strip()  # Obtener la query y evitar errores por None

    if query:
        # Normalizar la consulta: quitar tildes y convertir a mayúsculas
        query_normalized = normalize_and_uppercase(query)

        # Filtrar los resultados de la lista combinada según la búsqueda
        combined_list = [
            item
            for item in combined_list
            if (
                (
                    hasattr(item, "titulo")
                    and query_normalized in normalize_and_uppercase(item.titulo or "")
                )
                or (
                    hasattr(item, "codigo")
                    and query_normalized in normalize_and_uppercase(item.codigo or "")
                )
                or (
                    hasattr(item, "caracterizacion")
                    and query_normalized
                    in normalize_and_uppercase(item.caracterizacion or "")
                )
                or (
                    hasattr(item, "title")
                    and query_normalized in normalize_and_uppercase(item.title or "")
                )
            )
        ]

    # Paginación de los resultados combinados
    paginator = Paginator(combined_list, 20)
    page = request.GET.get("page")

    try:
        documentos = paginator.page(page)
    except PageNotAnInteger:
        documentos = paginator.page(1)
    except EmptyPage:
        documentos = paginator.page(paginator.num_pages)

    return render(
        request,
        "documentos/documentos.html",
        {"documentos": documentos, "query": query},
    )


@never_cache
@login_required_custom
def buscar_documentos(request):
    query = request.GET.get("q", "")
    documentos = Document.objects.filter(titulo__icontains=query)[
        :10
    ]  # Limita a 10 resultados
    resultados = [
        {
            "id": doc.id,
            "titulo": doc.titulo,
            "url": reverse("ver_pdf", args=[doc.id_archivo]),
        }
        for doc in documentos
    ]
    return JsonResponse(resultados, safe=False)


@never_cache
@login_required_custom
def download_file(request, document_id):
    # Cambia 'Document' por tu modelo correspondiente
    document = get_object_or_404(Document, id_archivo=document_id)
    file_path = document.file.path  # Cambia esto si estás usando otro campo

    if not os.path.exists(file_path):
        raise Http404("El archivo no fue encontrado.")

    with open(file_path, "rb") as file:
        response = HttpResponse(file.read(), content_type="application/octet-stream")
        response["Content-Disposition"] = (
            f'attachment; filename="{os.path.basename(file_path)}"'
        )

        # Agregar encabezados de seguridad
        response["Cross-Origin-Opener-Policy"] = "same-origin"
        response["Cross-Origin-Embedder-Policy"] = (
            "require-corp"  # Opcional, dependiendo de tus necesidades
        )

        return response


@never_cache
@login_required_custom
def download(request, pk):
    # Obtener el objeto Document
    document = get_object_or_404(Document, pk=pk)

    # Leer el archivo PDF original
    with open(document.file.path, "rb") as f:
        pdf_reader = PdfReader(f)
        pdf_writer = PdfWriter()

        # Crear un PDF temporal para la marca de agua
        watermark_buffer = BytesIO()
        c = canvas.Canvas(watermark_buffer)
        c.setFont("Helvetica", 50)  # Tamaño grande
        c.setFillColorRGB(0.5, 0.5, 0.5, alpha=0.3)  # Color gris y semi-transparente
        c.drawString(100, 400, "Copia no controlada")  # Ajusta la posición
        c.save()
        watermark_buffer.seek(0)

        # Leer la marca de agua
        watermark_reader = PdfReader(watermark_buffer)

        # Aplicar la marca de agua a cada página del PDF original
        for page in pdf_reader.pages:
            # Crear una nueva página que contiene la marca de agua
            page.merge_page(watermark_reader.pages[0])
            pdf_writer.add_page(page)

        # Guardar el PDF modificado en memoria
        response = HttpResponse(content_type="application/pdf")
        # Generar el nombre del archivo
        nameDocument = document.file.name.split("documents\\")[
            -1
        ]  # Usamos '\\' en Windows
        response["Content-Disposition"] = f'attachment; filename="{nameDocument}"'

        # Escribir el PDF modificado en la respuesta HTTP
        pdf_writer.write(response)

    return response


def convert_docx_to_pdf(docx_path, delete_after_use=True):
    """
    Convierte un archivo DOCX a PDF usando LibreOffice.

    Args:
        docx_path (str): Ruta del archivo DOCX de origen
        delete_after_use (bool): Si se debe eliminar el PDF después de usarlo

    Returns:
        str: Ruta del archivo PDF generado
    """
    # Verifica que el archivo DOCX exista
    if not os.path.exists(docx_path):
        raise FileNotFoundError(f"El archivo {docx_path} no existe")

    # Usa un directorio temporal si se requiere eliminación
    if delete_after_use:
        temp_dir = tempfile.mkdtemp()
        pdf_path = os.path.join(
            temp_dir, os.path.splitext(os.path.basename(docx_path))[0] + ".pdf"
        )
    else:
        pdf_path = docx_path.replace(".docx", ".pdf")

    # Comando para convertir el DOCX a PDF usando LibreOffice
    command = [
        "C:/Program Files/LibreOffice/program/soffice.exe",
        "--headless",
        "--convert-to",
        "pdf:writer_pdf_Export",  # Agregué esta configuración para exportación PDF
        "--outdir",
        os.path.dirname(pdf_path),
        docx_path,
    ]

    try:
        # Capturar salida para debugging
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Salida de conversión: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error al generar el PDF: {e}")
        print(f"Detalles del error: {e.stderr}")
        raise

    # Verificaciones adicionales
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"No se pudo generar el archivo PDF desde {docx_path}")

    # Verificar que el PDF no esté vacío
    if os.path.getsize(pdf_path) == 0:
        raise ValueError("El PDF generado está vacío")

    # Registra la eliminación del archivo temporal si es necesario
    if delete_after_use:

        def cleanup_pdf():
            try:
                os.unlink(pdf_path)
                os.rmdir(os.path.dirname(pdf_path))
            except Exception as e:
                print(f"Error al eliminar el PDF temporal: {e}")

        atexit.register(cleanup_pdf)

    return pdf_path


@login_required_custom
@xframe_options_exempt
def download_pdf_visualizar(request, id):
    # Obtén el documento desde la base de datos
    document = get_object_or_404(Document, id_archivo=id)

    # Ruta del archivo original
    file_path = document.file.path

    # Si el archivo es un .docx, lo convertimos a PDF antes de servirlo
    if file_path.endswith(".docx"):
        try:
            # Convertimos el DOCX a PDF y obtenemos la ruta del PDF generado
            pdf_path = convert_docx_to_pdf(file_path)
        except Exception as e:
            return HttpResponse(f"Error al generar el PDF: {str(e)}", status=500)
    else:
        # Si el archivo ya es un .pdf, usamos la ruta original
        pdf_path = file_path

    # Verificamos que el archivo PDF existe
    if not os.path.exists(pdf_path):
        return HttpResponse("El archivo PDF no existe", status=404)

    # Devuelve el archivo PDF como respuesta (inline para que se vea en el navegador)
    response = FileResponse(open(pdf_path, "rb"), content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="{os.path.basename(pdf_path)}"'

    return response


@login_required_custom
@xframe_options_exempt
def download_pdf_visualizar_solo_formato(request, id):
    # Obtén el documento desde la base de datos
    document = get_object_or_404(DocumentFormatosAsociados, id=id)

    # Ruta del archivo original
    file_path = document.file.path

    # Si el archivo es un .docx, lo convertimos a PDF antes de servirlo
    if file_path.endswith(".docx"):
        try:
            # Convertimos el DOCX a PDF y obtenemos la ruta del PDF generado
            pdf_path = convert_docx_to_pdf(file_path)
        except Exception as e:
            return HttpResponse(f"Error al generar el PDF: {str(e)}", status=500)
    else:
        # Si el archivo ya es un .pdf, usamos la ruta original
        pdf_path = file_path

    # Verificamos que el archivo PDF existe
    if not os.path.exists(pdf_path):
        return HttpResponse("El archivo PDF no existe", status=404)

    # Devuelve el archivo PDF como respuesta (inline para que se vea en el navegador)
    response = FileResponse(open(pdf_path, "rb"), content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="{os.path.basename(pdf_path)}"'

    return response


@never_cache
@login_required_custom
def download_generic(request, file_name):
    try:
        # Ruta completa al archivo en la carpeta 'uploads' dentro de 'media'
        file_path = os.path.join(settings.MEDIA_ROOT, "uploads", file_name)

        # Depuración: Muestra la ruta completa que se está generando
        print(f"Ruta del archivo: {file_path}")

        # Verifica si el archivo existe
        if not os.path.exists(file_path):
            print(
                f"Error: El archivo {file_name} no se encuentra en la ruta especificada."
            )
            return HttpResponse(f"Archivo no encontrado: {file_name}", status=404)

        # No es necesario abrir el archivo manualmente si se usa FileResponse
        print(f"El archivo {file_name} se ha encontrado y está listo para descargarse.")

        # Devolver el archivo con FileResponse
        response = FileResponse(open(file_path, "rb"), as_attachment=True)
        response["Content-Disposition"] = f'attachment; filename="{file_name}"'

        # Confirmación de que el archivo se está enviando
        print(f"Preparando la respuesta para descargar el archivo: {file_name}")

        return response

    except Exception as e:
        # Captura y muestra el error real
        print(f"Error al procesar el archivo: {str(e)}")
        return HttpResponse(f"Error al procesar el archivo: {str(e)}", status=500)


@never_cache
@login_required
def download_documents(request, document_id):
    try:
        # Buscar el documento por ID
        document = get_object_or_404(Document, id_archivo=document_id)

        # Obtener la ruta completa del archivo desde el campo 'file'
        file_path = document.file.path

        # Depuración: Muestra la ruta completa del archivo
        print(f"Ruta del archivo: {file_path}")

        # Verificar si el archivo existe
        if not os.path.exists(file_path):
            print(
                f"Error: El archivo {document.titulo} no se encuentra en la ruta especificada."
            )
            return HttpResponse(f"Archivo no encontrado: {document.titulo}", status=404)

        # Inicializar el nombre del documento con el nombre original
        nameDocument = document.file.name

        # Verificar si la ruta contiene 'uploads' o 'documents' para extraer el nombre relativo
        if "uploads" in file_path:
            nameDocument = file_path.split("uploads\\")[1]  # Usamos '\\' en Windows
        elif "documents" in file_path:
            nameDocument = file_path.split("documents\\")[1]  # Usamos '\\' en Windows

        # Devolver el archivo con FileResponse
        response = FileResponse(open(file_path, "rb"), as_attachment=True)
        response["Content-Disposition"] = f'attachment; filename="{nameDocument}"'

        # Confirmación de que el archivo se está enviando
        print(f"Preparando la respuesta para descargar el archivo: {nameDocument}")

        return response

    except Exception as e:
        print(f"Error al procesar el archivo: {str(e)}")
        return HttpResponse(f"Error al procesar el archivo: {str(e)}", status=500)


@never_cache
@login_required_custom
def download_format(request, document_id):
    try:
        # Buscar el documento por su ID
        document = get_object_or_404(DocumentFormatosAsociados, id=document_id)

        # Obtener la ruta del archivo desde el campo 'file'
        file_path = document.file.path

        # Depuración: Muestra la ruta completa del archivo
        print(f"Ruta del archivo: {file_path}")

        # Verificar si el archivo existe
        if not os.path.exists(file_path):
            print(
                f"Error: El archivo {document.title} no se encuentra en la ruta especificada."
            )
            return HttpResponse(f"Archivo no encontrado: {document.title}", status=404)
        nameDocument = document.file.name
        nameDocument = file_path.split("lib\\")[1]
        # Devolver el archivo con FileResponse
        response = FileResponse(open(file_path, "rb"), as_attachment=True)
        response["Content-Disposition"] = f'attachment; filename="{nameDocument}"'

        # Confirmación de que el archivo se está enviando
        print(f"Preparando la respuesta para descargar el archivo: {nameDocument}")

        return response

    except Exception as e:
        print(f"Error al procesar el archivo: {str(e)}")
        return HttpResponse(f"Error al procesar el archivo: {str(e)}", status=500)


# Funcion gemnerica para ver pdf solos en document
@never_cache
@login_required_custom
@xframe_options_exempt
def ver_pdf_solo(request, id):
    # Obtén el documento PDF
    document = get_object_or_404(Document, id_archivo=id)
    # Renderiza la plantilla y pasa el documento
    return render(request, "ver_pdf_solo.html", {"document": document})


# Funcion ver formatos en pdf en DocumentFormatosAsociados
@never_cache
@login_required_custom
@xframe_options_exempt
def ver_pdf_solo_formatos(request, id):
    # Obtén el documento PDF
    document = get_object_or_404(DocumentFormatosAsociados, id=id)
    # Renderiza la plantilla y pasa el documento
    return render(request, "ver_pdf_solo_formatos.html", {"document": document})


# Función genérica para ver PDF cons agregados
@never_cache
@login_required_custom
@xframe_options_exempt
def ver_pdf(request, id, model_name, image_form, formatos_form):
    document = get_object_or_404(Document, id_archivo=id)
    response = combined_view(
        request, document.id_archivo, model_name, image_form, formatos_form
    )  # Llama a images_view

    return response  # Retorna la respuesta de images_view


@never_cache
@login_required_custom
def combined_view(request, document_id, model_name, image_form, formatos_form):
    DocumentModel = apps.get_model("gestor_archivos", model_name)
    document = get_object_or_404(DocumentModel, id_archivo=document_id)

    try:
        images = getattr(document, image_form).all()
        formatos = getattr(document, formatos_form).all()
    except AttributeError:
        raise Http404("Las relaciones especificadas no existen en este documento")

    # Inicializar formularios
    image_form_class = getattr(forms, image_form, None)
    formatos_form_class = getattr(forms, formatos_form, None)

    if not image_form_class or not formatos_form_class:
        raise Http404("Formulario no encontrado")

    image_form_instance = image_form_class()
    formatos_form_instance = formatos_form_class()

    # Para obtener archivos y URLs específicos para cada formato
    formatos_data = []
    for formato in formatos:
        file_name = os.path.basename(formato.file.name) if formato.file else None
        url_name = os.path.basename(formato.file.url) if formato.file else None
        url_base = os.path.dirname(formato.file.url) if formato.file else None
        url_formato = f"{url_base}/{url_name}" if url_base and url_name else None
        formatos_data.append(
            {"formato": formato, "file_name": file_name, "url_formato": url_formato}
        )
        # este es el que no se diferencia
    if request.method == "POST":
        # Procesar formulario de imagen
        if "image_submit" in request.POST:
            image_form_instance = image_form_class(request.POST, request.FILES)
            if image_form_instance.is_valid():
                messages.success(request, "El diagrama se ha cargado correctamente.")
                image = image_form_instance.save(commit=False)
                image.document = document
                image.save()
                return redirect(
                    "ver_pdf",
                    id=document_id,
                    model_name=model_name,
                    image_form=image_form,
                    formatos_form=formatos_form,
                )

        # Procesar formulario de formatos
        if "formatos_submit" in request.POST:
            print("Formulario de formatos recibido")
            print("POST data completa:", dict(request.POST))
            print("FILES data:", request.FILES)

            formatos_form_instance = formatos_form_class(request.POST, request.FILES)

            # Depuración detallada de errores
            if not formatos_form_instance.is_valid():
                for field, errors in formatos_form_instance.errors.items():
                    print(f"Error en campo {field}: {errors}")

            if formatos_form_instance.is_valid():
                messages.success(request, "El formato se ha cargado correctamente.")
                formato_instance = formatos_form_instance.save(commit=False)
                formato_instance.document = document
                formato_instance.save()
                return redirect(
                    "ver_pdf",
                    id=document_id,
                    model_name=model_name,
                    image_form=image_form,
                    formatos_form=formatos_form,
                )
        # Actualización de archivo
        if "file" in request.FILES:
            nuevo_archivo = request.FILES["file"]
            if document.file:
                document.file.storage.delete(
                    document.file.name
                )  # Eliminar archivo anterior
            document.file = nuevo_archivo
            document.save()
            return redirect(
                "ver_pdf",
                id=document_id,
                model_name=model_name,
                image_form=image_form,
                formatos_form=formatos_form,
            )

    return render(
        request,
        "ver_pdf.html",
        {
            "document": document,
            "images": images,
            "image_form": image_form_instance,
            "formatos_data": formatos_data,  # Pasar la lista con los datos de los formatos
            "formatos_form": formatos_form_instance,
        },
    )


@never_cache
@login_required_custom
def delete_format(request, format_id, model_name, model_name_base, image_form):
    # Obtener el modelo usando el nombre desde la app
    DocumentModel = apps.get_model("documentacion", model_name)

    # Obtener el formato usando el ID proporcionado
    format_instance = get_object_or_404(DocumentModel, id=format_id)
    document_id = (
        format_instance.document.id_archivo
    )  # Obtener el ID del documento asociado

    # Obtener la ruta del archivo del formato
    format_file_path = format_instance.file.path  # Aquí accedemos al campo file

    try:
        # Eliminar el archivo del sistema de archivos
        if os.path.exists(format_file_path):
            os.remove(format_file_path)  # Elimina el archivo del sistema de archivos

        # Eliminar la entrada de la base de datos
        format_instance.delete()

        # Si la eliminación fue exitosa, devolver un JSON de éxito
        return JsonResponse(
            {"success": True, "message": f"El archivo ha sido eliminado correctamente."}
        )
    except Exception as e:
        # Si hay un error, devolver un JSON de error
        return JsonResponse({"success": False, "error": str(e)})


@never_cache
@login_required_custom
def delete_image(request, image_id, model_name, model_name_base, formatos_form):
    # Obtener el modelo usando el nombre desde la app 'documentacion'
    DocumentModel = apps.get_model("documentacion", model_name)

    # Obtener la imagen usando el ID proporcionado
    image = get_object_or_404(DocumentModel, id=image_id)
    document_id = image.document.id_archivo  # Obtener el ID del documento asociado

    # Obtener la ruta del archivo de imagen
    image_file_path = image.image.path  # Aquí accedemos al campo `image`

    try:
        # Eliminar el archivo del sistema de archivos
        if os.path.exists(image_file_path):
            os.remove(image_file_path)  # Elimina el archivo del sistema de archivos

        # Eliminar la entrada de la base de datos
        image.delete()

        # Si la eliminación fue exitosa, devolver un JSON de éxito
        return JsonResponse(
            {"success": True, "message": f"La imagen ha sido eliminada correctamente."}
        )
    except Exception as e:
        # Si hay un error, devolver un JSON de error
        return JsonResponse({"success": False, "error": str(e)})


# Politica de calidad ########################################
@never_cache
@login_required_custom
def politica_calidad(request):
    return render(request, "politica/politica.html")


@never_cache
@login_required_custom
def politica(request):
    return render(request, "politica/politica_calidad_integral.html")


@never_cache
@login_required_custom
def objetivos(request):
    return render(request, "politica/objetivos_politica.html")
