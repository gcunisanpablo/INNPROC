from django.shortcuts import render, redirect
import unicodedata
from django.views.decorators.cache import never_cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import (
    GlosarioForm,
)
from .models import Glosario
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Funcion verificacion logeado custom
def login_required_custom(view_func):
    return login_required(view_func, login_url="login")


# Función de normalización
def normalize_and_uppercase(input_string):
    """Normaliza el texto eliminando tildes y convirtiendo a mayúsculas."""
    return (
        unicodedata.normalize("NFD", input_string)
        .encode("ascii", "ignore")
        .decode("ascii")
        .upper()
    )


# Vista del glosario
@never_cache
@login_required_custom
def glosario(request):
    # Obtener todos los términos del glosario, ordenados por 'termino'
    glosario_list = Glosario.objects.all().order_by("termino")

    # Obtener la consulta de búsqueda
    query = request.GET.get(
        "q", ""
    ).strip()  # Obtener la query y evitar errores por None

    # Si hay una búsqueda
    if query:
        # Normalizar la consulta: quitar tildes y convertir a mayúsculas
        query_normalized = normalize_and_uppercase(query)

        # Filtrar los resultados del glosario según el término normalizado
        glosario_list = [
            item
            for item in glosario_list
            if query_normalized in normalize_and_uppercase(item.termino or "")
        ]

    # Paginación de los resultados filtrados
    paginator = Paginator(glosario_list, 20)
    page = request.GET.get("page")

    try:
        terminos = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número entero, muestra la primera página
        terminos = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera del rango (por ejemplo, 9999), muestra la última página
        terminos = paginator.page(paginator.num_pages)

    # Renderizar la plantilla con los términos filtrados y la búsqueda
    return render(
        request,
        "glosario.html",
        {"terminos": terminos, "query": query},
    )


@never_cache
@login_required_custom
def nuevo_termino(request):
    """Función para agregar un nuevo término al glosario"""
    if request.method == "POST":
        formulario = GlosarioForm(request.POST)

        if formulario.is_valid():
            termino = formulario.cleaned_data["termino"]

            # Normalizar el término ingresado
            termino_normalizado = normalize_and_uppercase(termino)

            # Verificar si el término normalizado ya existe en el glosario
            # Comparamos con términos normalizados
            if any(
                normalize_and_uppercase(g.termino) == termino_normalizado
                for g in Glosario.objects.all()
            ):
                # Usar messages para mostrar SweetAlert
                messages.error(request, "El término ya existe en el glosario.")
                return render(request, "nuevo_termino.html", {"formulario": formulario})

            # Guardar nuevo término
            glosario = Glosario(
                termino=termino,
                definicion=formulario.cleaned_data["definicion"],
            )
            glosario.save()
            messages.success(request, "Término agregado exitosamente.")
            return redirect("glosario")
    else:
        formulario = GlosarioForm()

    return render(request, "nuevo_termino.html", {"formulario": formulario})


@never_cache
@login_required_custom
def editar_termino(request, id):
    # Obtén el término que deseas editar
    termino = Glosario.objects.get(id_termino=id)

    # Crea el formulario, vinculando la instancia existente
    formulario = GlosarioForm(request.POST or None, instance=termino)

    # Verifica si la solicitud es POST
    if request.method == "POST":
        # Verifica si el formulario es válido
        if formulario.is_valid():
            formulario.save()  # Guarda los cambios
            messages.success(request, "Término Actualizado Correctamente.")
            return redirect("glosario")  # Cambia por la vista deseada

    # Renderiza el formulario (tanto en GET como si POST no es válido)
    return render(request, "editartermino.html", {"formulario": formulario})


@never_cache
@login_required_custom
def eliminar_termino(request, id):
    termino = Glosario.objects.get(id_termino=id)
    termino.delete()
    messages.success(request, "Término Eliminado exitosamente.")
    return redirect("glosario")
