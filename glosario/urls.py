from django.urls import path
from glosario import views

urlpatterns = [
    path("glosario/", views.glosario, name="glosario"),
    path("glosario/nuevo-termino/", views.nuevo_termino, name="nuevo-termino"),
    path(
        "glosario/editar-termino/<int:id>/", views.editar_termino, name="editar-termino"
    ),
    path(
        "glosario/eliminar-termino/<int:id>/",
        views.eliminar_termino,
        name="eliminar-termino",
    ),
]
