import json
import os
import time
from django.conf import settings
from django.utils.html import escape
from django.apps import apps
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from itertools import chain
from gestor_archivos.models import Document
from documentacion.models import DocumentFormatosAsociados
import re  # Usamos expresiones regulares para encontrar el id y el contenido dentro de cualquier etiqueta
from datetime import timedelta
from django.shortcuts import render, redirect
from .models import VideoTutorial
from .forms import VideoTutorialForm


# Funcion verificacion logeado custom
def login_required_custom(view_func):
    return login_required(view_func, login_url="login")


# Guardar contenido de HTMLS editables
@never_cache
@login_required
def save_content(request, model, folder_name, html_file_name):
    if request.method == "POST":
        try:
            # Intentar cargar los datos JSON
            data = json.loads(request.body)
            content_data = data.get("data", [])  # Obtener todos los campos a actualizar

            # Verificar si los datos son válidos
            if not content_data:
                return JsonResponse(
                    {"status": "fail", "error": "Invalid data"},
                    status=400,
                )

            # Guardar o actualizar el contenido en la base de datos
            for item in content_data:
                identifier = item.get("id")
                content = item.get("content")
                if identifier and content:
                    model.objects.update_or_create(
                        identifier=identifier, defaults={"content": content}
                    )

            # Ruta al archivo HTML, utilizando las variables dinámicas para la carpeta y archivo
            # En produccion desactivar esta opcion
            template_path = os.path.join(
                settings.BASE_DIR,
                "mapa_procesos",
                "templates",
                "procesos",
                folder_name,  # Aquí se pasa la carpeta dinámica
                html_file_name,  # Aquí se pasa el archivo dinámico
            )

            # Verificar si el archivo existe
            # En produccion desactivar esta opcion
            if not os.path.exists(template_path):
                return JsonResponse(
                    {
                        "status": "fail",
                        "error": f"El archivo no se encuentra en la ruta: {template_path}",
                    },
                    status=500,
                )

            try:
                # Leer el archivo HTML con reintentos si es necesario
                # En produccion desactivar esta opcion
                max_retries = 5
                attempt = 0
                html_content = ""

                while attempt < max_retries:
                    try:
                        with open(template_path, "r", encoding="utf-8") as f:
                            html_content = f.read()

                        if html_content:  # Si se leyó correctamente, salir del bucle
                            break
                    except IOError:
                        time.sleep(0.5)  # Esperar 500 ms antes de reintentar
                        attempt += 1

                # Si no se logró leer el archivo después de varios intentos, retornar un error
                # En produccion desactivar esta opcion
                if not html_content:
                    return JsonResponse(
                        {
                            "status": "fail",
                            "error": "El archivo HTML sigue vacío después de varios intentos.",
                        },
                        status=500,
                    )

                # Actualizar el contenido de cada identificador en el HTML
                # En produccion desactivar esta opcion
                for item in content_data:
                    identifier = item.get("id")
                    content = item.get("content")
                    if identifier and content:
                        content_value = escape(content)
                        pattern = re.compile(
                            r'(<[^>]*id=["\']){}(["][^>]*>)(.*?)(</[^>]+>)'.format(
                                re.escape(identifier)
                            ),
                            re.DOTALL,
                        )

                        match = pattern.search(html_content)

                        if match:
                            # Reemplazar el contenido
                            html_content = (
                                html_content[: match.start(3)]
                                + content_value
                                + html_content[match.end(3) :]
                            )
                # En produccion desactivar esta opcion
                # Guardar el archivo HTML solo si hubo cambios
                with open(template_path, "w", encoding="utf-8") as f:
                    f.write(html_content)

                return JsonResponse(
                    {
                        "status": "success",
                        "message": "Contenido actualizado correctamente.",
                    }
                )

            except Exception as e:
                return JsonResponse(
                    {
                        "status": "fail",
                        "error": f"Error al actualizar el HTML: {str(e)}",
                    },
                    status=500,
                )

        except json.JSONDecodeError:
            return JsonResponse({"status": "fail", "error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "fail", "error": str(e)}, status=500)

    return JsonResponse({"status": "fail"}, status=400)


# Obtener contenido de HTMLS editables
@never_cache
@login_required
def get_content(request, model):
    if request.method == "GET":
        try:
            # Obtener todos los contenidos del modelo
            contents = model.objects.all()
            data = {content.identifier: content.content for content in contents}

            # Retornar los datos en formato JSON
            return JsonResponse(data)
        except Exception as e:
            # Si ocurre un error al intentar obtener el contenido
            return JsonResponse({"status": "fail", "error": str(e)}, status=500)

    return JsonResponse({"status": "fail"}, status=400)


# Funcion llamada guardar contenido de HTMLS editables
@never_cache
@login_required
@csrf_exempt
def save_content_view(request, model_name, folder_name, html_file_name):
    try:
        # Obtener el modelo dinámicamente
        model = apps.get_model("mapa_procesos", model_name)
        return save_content(request, model, folder_name, html_file_name)
    except LookupError:
        return JsonResponse({"status": "fail", "error": "Model not found"}, status=404)


# Funcion llamada obtener contenido de HTMLS editables
@never_cache
@login_required
@csrf_exempt
def get_content_view(request, model_name):
    try:
        # Obtener el modelo dinámicamente
        model = apps.get_model("mapa_procesos", model_name)
        return get_content(request, model)
    except LookupError:
        return JsonResponse({"status": "fail", "error": "Model not found"}, status=404)


# Lista de novedades
@never_cache
@login_required_custom
def mapa_procesos(request):
    # Manejo del formulario de tutoriales
    if request.method == "POST":
        form = VideoTutorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mapa-procesos")
    else:
        form = VideoTutorialForm()

    # Obtener todos los documentos de ambos modelos
    documentos_list = Document.objects.all().order_by("-fecha_creacion")
    formatos_list = DocumentFormatosAsociados.objects.all().order_by("-fecha_creacion")

    # Obtener videos
    tutorials = VideoTutorial.objects.all()

    # Filtrar los archivos con extensión .pdf o .docx y sin la palabra "procedimiento" en el título
    documentos_list = [
        doc
        for doc in documentos_list
        if doc.file.name.endswith((".pdf", ".docx"))
        and "procedimiento" not in doc.titulo.lower()
    ]

    formatos_list = [
        formato
        for formato in formatos_list
        if formato.file.name.endswith((".pdf", ".docx"))
    ]

    # Combinar ambas listas
    combined_list = list(chain(documentos_list, formatos_list))

    # Restar 5 horas de la fecha_creacion para cada documento
    for item in combined_list:
        item.fecha_creacion = item.fecha_creacion - timedelta(hours=5)

    # Limitar a los últimos 4 documentos
    ultimos_4_documentos = combined_list[:3]

    # Pasar todos los datos necesarios al template
    context = {
        "ultimos_archivos": ultimos_4_documentos,
        "tutorials": tutorials,
        "form": form,
    }

    return render(request, "mapa_procesos.html", context)


from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse


def eliminar_tutorial(request, tutorial_id):
    tutorial = get_object_or_404(VideoTutorial, id=tutorial_id)
    tutorial.delete()
    return redirect(reverse("mapa-procesos"))  # O cambia a donde quieras redirigir


# HTMLS Mapa de procesos primer paso
# PROCESOS MISIONALES
# =============================================================================#
@never_cache
@login_required_custom
def docencia_calidad(request):
    return render(request, "docencia_calidad.html")


##############################################################
@never_cache
@login_required_custom
def desarrollo_curricular(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/docencia_calidad/desarrollo_curricular.html",
        context,
    )


##############################################################
@never_cache
@login_required_custom
def enseñanza_prendizaje_evaluacion(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/docencia_calidad/enseñanza_prendizaje_evaluacion.html",
        context,
    )


##############################################################


# =============================================================================#
@never_cache
@login_required_custom
def investigacion_pertinente(request):
    return render(request, "investigacion_pertinente.html")


##############################################################
@never_cache
@login_required_custom
def gestion_investigacion(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/investigacion_pertinente/gestion_investigacion.html",
        context,
    )


##############################################################


# =============================================================================#
@never_cache
@login_required_custom
def proyeccion_social_impacto(request):
    return render(request, "proyeccion_social_impacto.html")


##############################################################
@never_cache
@login_required_custom
def extension_proyeccion(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/proyeccion_social_impacto/extension_proyeccion.html",
        context,
    )


##############################################################
@never_cache
@login_required_custom
def relacionamineto_egresados(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/proyeccion_social_impacto/relacionamineto_egresados.html",
        context,
    )


##############################################################


# PROCESOS DE APOYO
# =============================================================================#
@never_cache
@login_required_custom
def gestion_infraestructura_fisica_tecnologica(request):
    return render(request, "gestion_infraestructura_fisica_tecnologica.html")


##############################################################
@never_cache
@login_required_custom
def gestion_sistemas_comunicacion(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/gestion_infraestructura_fisica_tecnologica/gestion_sistemas_comunicacion.html",
        context,
    )


##############################################################
@never_cache
@login_required_custom
def informacion_bibliografica(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/gestion_infraestructura_fisica_tecnologica/informacion_bibliografica.html",
        context,
    )


##############################################################
@never_cache
@login_required_custom
def infraestructura_fisica(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/gestion_infraestructura_fisica_tecnologica/infraestructura_fisica.html",
        context,
    )


##############################################################


# =============================================================================#
@never_cache
@login_required_custom
def gestion_administrativa_financiera(request):
    return render(request, "gestion_administrativa_financiera.html")


##############################################################
@never_cache
@login_required_custom
def gestion_cartera(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/gestion_administrativa_financiera/gestion_cartera.html",
        context,
    )


##############################################################
@never_cache
@login_required_custom
def gestion_recursos_financieros(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/gestion_administrativa_financiera/gestion_recursos_financieros.html",
        context,
    )


################################################################
@never_cache
@login_required_custom
def gestion_documental(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/gestion_administrativa_financiera/gestion_documental.html",
        context,
    )


################################################################
# =============================================================================#
@never_cache
@login_required_custom
def gestion_mercadeo_admisiones(request):
    return render(request, "gestion_mercadeo_admisiones.html")


##############################################################
@never_cache
@login_required_custom
def admisiones_registro_control(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/gestion_mercadeo_admisiones/admisiones_registro_control.html",
        context,
    )


# ===============================================================================#
@never_cache
@login_required_custom
def gestion_juridica_contractual(request):
    return render(request, "gestion_juridica_contractual.html")


#######################################################################################
@never_cache
@login_required_custom
def gestion_juridica(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/gestion_juridica_contractual/gestion_juridica.html",
        context,
    )


##########################################################################################
@never_cache
@login_required_custom
def gestion_contractual(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/gestion_juridica_contractual/gestion_contractual.html",
        context,
    )


##########################################################################################
# DIRECCIONAMINETO ESTRATEGICO
# =============================================================================#
@never_cache
@login_required_custom
def talento_humano_bienestar(request):
    return render(request, "talento_humano_bienestar.html")


##########################################################################################
@never_cache
@login_required_custom
def bienestar_institucional(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/talento_humano_bienestar/bienestar_institucional.html",
        context,
    )


##########################################################################################
@never_cache
@login_required_custom
def control_disciplinario(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/talento_humano_bienestar/control_disciplinario.html",
        context,
    )


##########################################################################################
@never_cache
@login_required_custom
def gestion_desarrollo_humano(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/talento_humano_bienestar/gestion_desarrollo_humano.html",
        context,
    )


##########################################################################################


# =============================================================================#
@never_cache
@login_required_custom
def calidad_integral(request):
    return render(request, "calidad_integral.html")


##########################################################################################
@never_cache
@login_required_custom
def aseguramiento_calidad_academica(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/calidad_integral/aseguramiento_calidad_academica.html",
        context,
    )


##########################################################################################
@never_cache
@login_required_custom
def aseguramiento_calidad_procesos(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/calidad_integral/aseguramiento_calidad_procesos.html",
        context,
    )


##########################################################################################
@never_cache
@login_required_custom
def auditorias(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/calidad_integral/auditorias.html",
        context,
    )


##########################################################################################
@never_cache
@login_required_custom
def evaluacion_control(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/calidad_integral/evaluacion_control.html",
        context,
    )


##########################################################################################
@never_cache
@login_required_custom
def gestion_integrada(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/calidad_integral/gestion_integrada.html",
        context,
    )


##########################################################################################
@never_cache
@login_required_custom
def gestion_registro_calificado(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/calidad_integral/gestion_registro_calificado.html",
        context,
    )


##########################################################################################
@never_cache
@login_required_custom
def gestion_servicio_usuario(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/calidad_integral/gestion_servicio_usuario.html",
        context,
    )


##########################################################################################


# =============================================================================#
@never_cache
@login_required_custom
def relaciones_internacionales(request):
    return render(request, "relaciones_internacionales.html")


##########################################################################################
@never_cache
@login_required_custom
def comunicacion(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/relaciones_internacionales/comunicacion.html",
        context,
    )


##########################################################################################
@never_cache
@login_required_custom
def internacionalizacion(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/relaciones_internacionales/internacionalizacion.html",
        context,
    )


##########################################################################################
# =============================================================================#
@never_cache
@login_required_custom
def planeacion_estrategica(request):
    return render(request, "planeacion_estrategica.html")


##########################################################################################
@never_cache
@login_required_custom
def gestion_informacion(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/planeacion_estrategica/gestion_informacion.html",
        context,
    )


##########################################################################################
@never_cache
@login_required_custom
def planeacion_estrategica_institucional(request):
    context = {
        "is_superuser": request.user.is_authenticated and request.user.is_superuser,
    }
    return render(
        request,
        "procesos/planeacion_estrategica/planeacion_estrategica_institucional.html",
        context,
    )


##########################################################################################
