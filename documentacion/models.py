import datetime
from django.db import models
from gestor_archivos.models import (
    Document_admisiones_registro_control,
    Document_gestion_documental,
    Document_gestion_cartera,
    Document_gestion_recursos_financieros,
    Document_gestion_contractual,
    Document_gestion_juridica,
    Document_infraestructura_fisica,
    Document_gestion_sistemas_comunicacion,
    Document_gestion_investigacion,
    Document_enseñanza_prendizaje_evaluacion,
    Document_desarrollo_curricular,
    Document_extension_proyeccion,
    Document_relacionamineto_egresados,
    Document_planeacion_estrategica_institucional,
    Document_gestion_informacion,
    Document_aseguramiento_calidad_academica,
    Document_aseguramiento_calidad_procesos,
    Document_auditorias,
    Document_evaluacion_control,
    Document_gestion_integrada,
    Document_gestion_registro_calificado,
    Document_gestion_servicio_usuario,
    Document_comunicacion,
    Document_internacionalizacion,
    Document_bienestar_institucional,
    Document_control_disciplinario,
    Document_gestion_desarrollo_humano,
)


# Documentos asociadas diagramas
class DocumentAsociadosDiagramasFlujo(models.Model):
    image = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)


# Diagramas asociados a documentos asociados especificos de caracterizacion//////


class DocumentImage_admisiones_registro_control(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_admisiones_registro_control,
        on_delete=models.CASCADE,
        related_name="DocumentImage_admisiones_registro_control",
    )

    class Meta:
        db_table = (
            # imagenes asociadas al documento asociado
            "DocumentImage_admisiones_registro_control"
            # Nombre de la tabla en la base de datos
        )


class DocumentImage_gestion_documental(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_gestion_documental,
        on_delete=models.CASCADE,
        related_name="DocumentImage_gestion_documental",
    )

    class Meta:
        db_table = "DocumentImage_gestion_documental"


class DocumentImage_gestion_cartera(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_gestion_cartera,
        on_delete=models.CASCADE,
        related_name="DocumentImage_gestion_cartera",
    )

    class Meta:
        db_table = "DocumentImage_gestion_cartera"


class DocumentImage_gestion_recursos_financieros(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_gestion_recursos_financieros,
        on_delete=models.CASCADE,
        related_name="DocumentImage_gestion_recursos_financieros",
    )

    class Meta:
        db_table = "DocumentImage_gestion_recursos_financieros"


class DocumentImage_gestion_contractual(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_gestion_contractual,
        on_delete=models.CASCADE,
        related_name="DocumentImage_gestion_contractual",
    )

    class Meta:
        db_table = "DocumentImage_gestion_contractual"


class DocumentImage_gestion_juridica(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_gestion_juridica,
        on_delete=models.CASCADE,
        related_name="DocumentImage_gestion_juridica",
    )

    class Meta:
        db_table = "DocumentImage_gestion_juridica"


class DocumentImage_infraestructura_fisica(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_infraestructura_fisica,
        on_delete=models.CASCADE,
        related_name="DocumentImage_infraestructura_fisica",
    )

    class Meta:
        db_table = "DocumentImage_infraestructura_fisica"


class DocumentImage_gestion_sistemas_comunicacion(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_gestion_sistemas_comunicacion,
        on_delete=models.CASCADE,
        related_name="DocumentImage_gestion_sistemas_comunicacion",
    )

    class Meta:
        db_table = "DocumentImage_gestion_sistemas_comunicacion"


class DocumentImage_gestion_investigacion(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_gestion_investigacion,
        on_delete=models.CASCADE,
        related_name="DocumentImage_gestion_investigacion",
    )

    class Meta:
        db_table = "DocumentImage_gestion_investigacion"


class DocumentImage_enseñanza_prendizaje_evaluacion(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_enseñanza_prendizaje_evaluacion,
        on_delete=models.CASCADE,
        related_name="DocumentImage_enseñanza_prendizaje_evaluacion",
    )

    class Meta:
        db_table = "DocumentImage_enseñanza_prendizaje_evaluacion"


class DocumentImage_desarrollo_curricular(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_desarrollo_curricular,
        on_delete=models.CASCADE,
        related_name="DocumentImage_desarrollo_curricular",
    )

    class Meta:
        db_table = "DocumentImage_desarrollo_curricular"


class DocumentImage_extension_proyeccion(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_extension_proyeccion,
        on_delete=models.CASCADE,
        related_name="DocumentImage_extension_proyeccion",
    )

    class Meta:
        db_table = "DocumentImage_extension_proyeccion"


class DocumentImage_relacionamineto_egresados(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_relacionamineto_egresados,
        on_delete=models.CASCADE,
        related_name="DocumentImage_relacionamineto_egresados",
    )

    class Meta:
        db_table = "DocumentImage_relacionamineto_egresados"


class DocumentImage_planeacion_estrategica_institucional(
    DocumentAsociadosDiagramasFlujo
):
    document = models.ForeignKey(
        Document_planeacion_estrategica_institucional,
        on_delete=models.CASCADE,
        related_name="DocumentImage_planeacion_estrategica_institucional",
    )

    class Meta:
        db_table = "DocumentImage_planeacion_estrategica_institucional"


class DocumentImage_gestion_informacion(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_gestion_informacion,
        on_delete=models.CASCADE,
        related_name="DocumentImage_gestion_informacion",
    )

    class Meta:
        db_table = "DocumentImage_gestion_informacion"


class DocumentImage_aseguramiento_calidad_academica(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_aseguramiento_calidad_academica,
        on_delete=models.CASCADE,
        related_name="DocumentImage_aseguramiento_calidad_academica",
    )

    class Meta:
        db_table = "DocumentImage_aseguramiento_calidad_academica"


class DocumentImage_aseguramiento_calidad_procesos(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_aseguramiento_calidad_procesos,
        on_delete=models.CASCADE,
        related_name="DocumentImage_aseguramiento_calidad_procesos",
    )

    class Meta:
        db_table = "DocumentImage_aseguramiento_calidad_procesos"


class DocumentImage_auditorias(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_auditorias,
        on_delete=models.CASCADE,
        related_name="DocumentImage_auditorias",
    )

    class Meta:
        db_table = "DocumentImage_auditorias"


class DocumentImage_evaluacion_control(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_evaluacion_control,
        on_delete=models.CASCADE,
        related_name="DocumentImage_evaluacion_control",
    )

    class Meta:
        db_table = "DocumentImage_evaluacion_control"


class DocumentImage_gestion_integrada(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_gestion_integrada,
        on_delete=models.CASCADE,
        related_name="DocumentImage_gestion_integrada",
    )

    class Meta:
        db_table = "DocumentImage_gestion_integrada"


class DocumentImage_gestion_registro_calificado(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_gestion_registro_calificado,
        on_delete=models.CASCADE,
        related_name="DocumentImage_gestion_registro_calificado",
    )

    class Meta:
        db_table = "DocumentImage_gestion_registro_calificado"


class DocumentImage_gestion_servicio_usuario(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_gestion_servicio_usuario,
        on_delete=models.CASCADE,
        related_name="DocumentImage_gestion_servicio_usuario",
    )

    class Meta:
        db_table = "DocumentImage_gestion_servicio_usuario"


class DocumentImage_comunicacion(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_comunicacion,
        on_delete=models.CASCADE,
        related_name="DocumentImage_comunicacion",
    )

    class Meta:
        db_table = "DocumentImage_comunicacion"


class DocumentImage_internacionalizacion(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_internacionalizacion,
        on_delete=models.CASCADE,
        related_name="DocumentImage_internacionalizacion",
    )

    class Meta:
        db_table = "DocumentImage_internacionalizacion"


class DocumentImage_bienestar_institucional(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_bienestar_institucional,
        on_delete=models.CASCADE,
        related_name="DocumentImage_bienestar_institucional",
    )

    class Meta:
        db_table = "DocumentImage_bienestar_institucional"


class DocumentImage_control_disciplinario(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_control_disciplinario,
        on_delete=models.CASCADE,
        related_name="DocumentImage_control_disciplinario",
    )

    class Meta:
        db_table = "DocumentImage_control_disciplinario"


class DocumentImage_gestion_desarrollo_humano(DocumentAsociadosDiagramasFlujo):
    document = models.ForeignKey(
        Document_gestion_desarrollo_humano,
        on_delete=models.CASCADE,
        related_name="DocumentImage_gestion_desarrollo_humano",
    )

    class Meta:
        db_table = "DocumentImage_gestion_desarrollo_humano"


# Modelo para formatos de documetos asociados


class DocumentFormatosAsociados(models.Model):
    title = models.CharField(max_length=255)
    codigo = models.CharField(max_length=100)
    caracterizacion = models.CharField(max_length=100)
    procedimiento = models.CharField(max_length=100)
    file = models.FileField(max_length=200, upload_to="lib/", verbose_name="Archivo")
    fecha_creacion = models.DateTimeField(
        default=datetime.datetime.now().replace(microsecond=0)
    )


# Formatos asociados a documentos asociados especificos de caracterizacion ////////


class DocumentDoAs_admisiones_registro_control_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_admisiones_registro_control,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_admisiones_registro_control_FoAs",
    )

    class Meta:
        db_table = (
            # Formatos asociados admisiones_registro_control
            "DocumentDoAs_admisiones_registro_control_FoAs"
            # Nombre de la tabla en la base de datos
        )


class DocumentDoAs_gestion_documental_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_gestion_documental,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_gestion_documental_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_gestion_documental_FoAs"


class DocumentDoAs_gestion_cartera_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_gestion_cartera,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_gestion_cartera_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_gestion_cartera_FoAs"


class DocumentDoAs_gestion_recursos_financieros_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_gestion_recursos_financieros,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_gestion_recursos_financieros_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_gestion_recursos_financieros_FoAs"


class DocumentDoAs_gestion_contractual_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_gestion_contractual,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_gestion_contractual_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_gestion_contractual_FoAs"


class DocumentDoAs_gestion_juridica_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_gestion_juridica,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_gestion_juridica_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_gestion_juridica_FoAs"


class DocumentDoAs_infraestructura_fisica_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_infraestructura_fisica,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_infraestructura_fisica_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_infraestructura_fisica_FoAs"


class DocumentDoAs_gestion_sistemas_comunicacion_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_gestion_sistemas_comunicacion,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_gestion_sistemas_comunicacion_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_gestion_sistemas_comunicacion_FoAs"


class DocumentDoAs_gestion_investigacion_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_gestion_investigacion,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_gestion_investigacion_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_gestion_investigacion_FoAs"


class DocumentDoAs_enseñanza_prendizaje_evaluacion_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_enseñanza_prendizaje_evaluacion,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_enseñanza_prendizaje_evaluacion_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_enseñanza_prendizaje_evaluacion_FoAs"


class DocumentDoAs_desarrollo_curricular_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_desarrollo_curricular,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_desarrollo_curricular_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_desarrollo_curricular_FoAs"


class DocumentDoAs_extension_proyeccion_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_extension_proyeccion,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_extension_proyeccion_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_extension_proyeccion_FoAs"


class DocumentDoAs_relacionamineto_egresados_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_relacionamineto_egresados,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_relacionamineto_egresados_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_relacionamineto_egresados_FoAs"


class DocumentDoAs_planeacion_estrategica_institucional_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_planeacion_estrategica_institucional,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_planeacion_estrategica_institucional_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_planeacion_estrategica_institucional_FoAs"


class DocumentDoAs_gestion_informacion_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_gestion_informacion,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_gestion_informacion_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_gestion_informacion_FoAs"


class DocumentDoAs_aseguramiento_calidad_academica_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_aseguramiento_calidad_academica,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_aseguramiento_calidad_academica_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_aseguramiento_calidad_academica_FoAs"


class DocumentDoAs_aseguramiento_calidad_procesos_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_aseguramiento_calidad_procesos,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_aseguramiento_calidad_procesos_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_aseguramiento_calidad_procesos_FoAs"


class DocumentDoAs_auditorias_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_auditorias,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_auditorias_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_auditorias_FoAs"


class DocumentDoAs_evaluacion_control_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_evaluacion_control,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_evaluacion_control_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_evaluacion_control_FoAs"


class DocumentDoAs_gestion_integrada_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_gestion_integrada,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_gestion_integrada_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_gestion_integrada_FoAs"


class DocumentDoAs_gestion_registro_calificado_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_gestion_registro_calificado,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_gestion_registro_calificado_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_gestion_registro_calificado_FoAs"


class DocumentDoAs_gestion_servicio_usuario_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_gestion_servicio_usuario,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_gestion_servicio_usuario_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_gestion_servicio_usuario_FoAs"


class DocumentDoAs_comunicacion_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_comunicacion,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_comunicacion_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_comunicacion_FoAs"


class DocumentDoAs_internacionalizacion_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_internacionalizacion,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_internacionalizacion_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_internacionalizacion_FoAs"


class DocumentDoAs_bienestar_institucional_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_bienestar_institucional,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_bienestar_institucional_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_bienestar_institucional_FoAs"


class DocumentDoAs_control_disciplinario_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_control_disciplinario,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_control_disciplinario_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_control_disciplinario_FoAs"


class DocumentDoAs_gestion_desarrollo_humano_FoAs(DocumentFormatosAsociados):
    document = models.ForeignKey(
        Document_gestion_desarrollo_humano,
        on_delete=models.CASCADE,
        related_name="DocumentDoAs_gestion_desarrollo_humano_FoAs",
    )

    class Meta:
        db_table = "DocumentDoAs_gestion_desarrollo_humano_FoAs"
