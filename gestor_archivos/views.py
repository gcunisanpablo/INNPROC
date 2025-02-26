from django.apps import apps
import os
from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from gestor_archivos import forms
from django.http import HttpResponse
from .models import Document
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt


# Función de verificación de inicio de sesión
def login_required_custom(view_func):
    return login_required(view_func, login_url="login")


@csrf_exempt
def save_html(request):
    # Verificar que la solicitud sea POST
    if request.method != "POST":
        print("Error: El método HTTP no permitido. Se requiere POST.")
        return JsonResponse(
            {"error": "Método HTTP no permitido, se requiere POST."}, status=405
        )

    # Verificar que el archivo PDF esté presente en los datos de la solicitud
    if not request.FILES.get("file"):
        print("Error: Falta el archivo PDF en la solicitud.")
        return JsonResponse(
            {"error": "Falta el archivo PDF en la solicitud."}, status=400
        )

    # Obtener los datos del formulario
    file = request.FILES["file"]
    codigo = request.POST.get("codigo")
    titulo = request.POST.get("titulo")
    caracterizacion = request.POST.get("caracterizacion")

    # Comprobar que todos los campos requeridos estén presentes
    if not codigo:
        print("Error: El campo 'codigo' está vacío.")
        return JsonResponse(
            {"error": 'El campo "codigo" es obligatorio y está vacío.'}, status=400
        )
    if not titulo:
        print("Error: El campo 'titulo' está vacío.")
        return JsonResponse(
            {"error": 'El campo "titulo" es obligatorio y está vacío.'}, status=400
        )
    if not caracterizacion:
        print("Error: El campo 'caracterizacion' está vacío.")
        return JsonResponse(
            {"error": 'El campo "caracterizacion" es obligatorio y está vacío.'},
            status=400,
        )

    # Comprobar que el archivo PDF es del tipo correcto
    if not file.name.endswith(".pdf"):
        print(f"Error: El archivo no es un PDF. El archivo recibido es {file.name}.")
        return JsonResponse({"error": "El archivo debe ser un PDF."}, status=400)

    try:
        # Crear el objeto Document con los datos recibidos
        document = Document(
            codigo=codigo, titulo=titulo, caracterizacion=caracterizacion, file=file
        )

        # Guardar el documento en la base de datos
        document.save()

        # Respuesta exitosa con el ID del documento guardado
        print(f"Documento guardado con éxito! ID del documento: {document.id_archivo}")
        return JsonResponse(
            {
                "message": "Documento guardado exitosamente!",
                "id_archivo": document.id_archivo,
            },
            status=200,
        )

    except ValidationError as e:
        # Capturar errores de validación y enviarlos como respuesta
        print(f"Error de validación: {str(e)}")
        return JsonResponse({"error": f"Error de validación: {str(e)}"}, status=400)
    except Exception as e:
        # Capturar cualquier otro error y enviarlo como respuesta
        print(f"Error al guardar el documento: {str(e)}")
        return JsonResponse(
            {"error": f"Error al guardar el documento: {str(e)}"}, status=500
        )


# Función genérica para crear documentos
@never_cache
@login_required
def crear_documento(request, model_name, form_name):
    try:
        # Obtener el modelo y el formulario usando los nombres
        DocumentModel = apps.get_model("gestor_archivos", model_name)
        # Importar el formulario específico
        DocumentForm = getattr(forms, form_name)

        if request.method == "POST":
            formulario = DocumentForm(request.POST, request.FILES)

            if formulario.is_valid():
                documento = DocumentModel(
                    codigo=formulario.cleaned_data["codigo"],
                    caracterizacion=formulario.cleaned_data["caracterizacion"],
                    titulo=formulario.cleaned_data["titulo"],
                    file=formulario.cleaned_data["file"],
                )
                documento.save()
                return JsonResponse(
                    {"success": True, "message": "Documento creado exitosamente."}
                )

            return JsonResponse({"success": False, "errors": formulario.errors})

        # Para GET, cargar el formulario
        formulario = DocumentForm()
        return render(request, "creardocumento.html", {"formulario": formulario})

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})


# Función genérica para eliminar documentos
@never_cache
@login_required
def eliminar_documento(request, model_name, id):
    try:
        # Obtener el modelo usando el nombre
        DocumentModel = apps.get_model("gestor_archivos", model_name)

        # Obtener el documento a eliminar
        documento = DocumentModel.objects.get(id_archivo=id)

        # Si el documento tiene un archivo asociado, lo eliminamos
        if documento.file:  # Verificar que el archivo existe
            document_path = documento.file.path
            try:
                if os.path.exists(document_path):
                    os.remove(document_path)  # Eliminar el archivo físico
                else:
                    messages.warning(request, "El archivo asociado no existe.")
            except Exception as e:
                messages.error(request, f"Error al eliminar el archivo: {str(e)}")
                return redirect("documentos")

        # Ahora eliminamos el objeto de la base de datos
        documento.delete()

        # Mensaje de éxito
        messages.success(request, "El documento ha sido eliminado exitosamente.")
    except DocumentModel.DoesNotExist:
        messages.error(request, "El documento no existe.")
    except Exception as e:
        messages.error(request, f"Ocurrió un error al eliminar el documento: {str(e)}")

    # Redirigir a la lista de documentos
    return redirect("documentos")


# LISTA TABLA ESPECIFICA
@never_cache
@login_required_custom
def lista_documentos_especificos(request, model_name):
    try:
        # Obtener el modelo usando el nombre
        DocumentModel = apps.get_model("gestor_archivos", model_name)

        # Obtener todos los documentos del modelo específico
        documentos = DocumentModel.objects.all()

        return render(
            request,
            "lista_documentos_especificos.html",
            {"documentos": documentos},
        )
    except Exception as e:
        # Solo retorna el mensaje de error en lugar de renderizar una página HTML
        return HttpResponse(f"Error: {str(e)}", status=500)


# LISTA TABLA ESPECIFICA globales
@never_cache
@login_required_custom
def lista_requisitos_legales_normativos_epecificos(request, model_name):
    try:
        # Obtener el modelo usando el nombre
        DocumentModel = apps.get_model("gestor_archivos", model_name)

        # Obtener todos los documentos del modelo específico
        documentos = DocumentModel.objects.all()

        return render(
            request,
            "lista_requisitos_legales_normativos_epecificos.html",
            {"documentos": documentos},
        )
    except Exception as e:
        # Solo retorna el mensaje de error en lugar de renderizar una página HTML
        return HttpResponse(f"Error: {str(e)}", status=500)


# LISTA TABLA ESPECIFICA globales
@never_cache
@login_required_custom
def lista_requisitos_necesidades_partes_interesadas_epecificos(request, model_name):
    try:
        # Obtener el modelo usando el nombre
        DocumentModel = apps.get_model("gestor_archivos", model_name)

        # Obtener todos los documentos del modelo específico
        documentos = DocumentModel.objects.all()

        return render(
            request,
            "lista_requisitos_necesidades_partes_interesadas_epecificos.html",
            {"documentos": documentos},
        )
    except Exception as e:
        # Solo retorna el mensaje de error en lugar de renderizar una página HTML
        return HttpResponse(f"Error: {str(e)}", status=500)


# LISTA TABLA ESPECIFICA INDICADORES
@never_cache
@login_required_custom
def lista_indicadores_especificos(request, model_name):
    try:
        # Obtener el modelo usando el nombre
        DocumentModel = apps.get_model("gestor_archivos", model_name)

        # Obtener todos los documentos del modelo específico
        documentos = DocumentModel.objects.all()

        return render(
            request,
            "lista_indicadores_especificos.html",
            {"documentos": documentos},
        )
    except Exception as e:
        # Solo retorna el mensaje de error en lugar de renderizar una página HTML
        return HttpResponse(f"Error: {str(e)}", status=500)


@never_cache
@login_required_custom
def cargar_imagen(request, model_name, form_name):
    # Importar el formulario específico
    DocumentForm = getattr(forms, form_name)
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guarda la imagen en la base de datos
            return redirect(
                "lista_img", model_name=model_name
            )  # Redirigir a otra vista después de guardar
    else:
        form = DocumentForm()

    return render(
        request, "form_img.html", {"form": form}
    )  # Cambia 'tu_template.html' al nombre de tu template


@never_cache
@login_required_custom
def eliminar_imagen(request, model_name, id):
    print(f"Recibiendo solicitud DELETE para el modelo {model_name} con id {id}")

    try:
        # Obtener el modelo dinámicamente usando el nombre
        DocumentModel = apps.get_model("gestor_archivos", model_name)
        print(f"Modelo cargado: {DocumentModel}")

        # Buscar el objeto con el id dado en el modelo
        imagen = get_object_or_404(DocumentModel, id=id)
        print(f"Imagen encontrada: {imagen.image.path}")

        # Verificar la ruta del archivo físico
        image_path = imagen.image.path

        # Comprobar si el archivo existe en la ruta
        if os.path.exists(image_path):
            os.remove(image_path)  # Eliminar el archivo físico
            print(f"Archivo eliminado: {image_path}")
        else:
            print(f"El archivo no existe: {image_path}")

        # Eliminar el objeto de la base de datos (imagen)
        imagen.delete()
        print(f"Imagen con id {id} eliminada de la base de datos.")

        # Aquí estamos devolviendo el JsonResponse y al mismo tiempo imprimiendo en la consola
        print("Respuesta JSON enviada con éxito.")
        return JsonResponse({"success": True})

    except Exception as e:
        # Si hay un error, lo capturamos y lo mostramos en los logs
        print(f"Error al eliminar la imagen: {e}")
        return JsonResponse({"success": False, "error": str(e)}, status=500)


@never_cache
@login_required_custom
def lista_img(request, model_name):
    # Obtener el modelo usando el nombre
    DocumentModel = apps.get_model("gestor_archivos", model_name)
    documentos = DocumentModel.objects.all()
    return render(request, "lista_img_especificas.html", {"documentos": documentos})


@never_cache
@login_required_custom
def detalle_img(request, model_name, img_id):
    # Obtener el modelo usando el nombre
    DocumentModel = apps.get_model("gestor_archivos", model_name)
    documento = get_object_or_404(DocumentModel, id=img_id)
    return render(request, "ver_img.html", {"documento": documento})
