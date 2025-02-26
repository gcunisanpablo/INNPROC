import os
from django.db import models
from django.utils import timezone


class Document(models.Model):
    id_archivo = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=30, unique=True)
    titulo = models.CharField(max_length=100, verbose_name="Título")
    caracterizacion = models.CharField(
        max_length=50, blank=True, verbose_name="Caracterizacion"
    )
    file = models.FileField(
        max_length=200, upload_to="documents/", verbose_name="Archivo"
    )
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.codigo:
            raise ValueError(
                "El campo 'codigo' es obligatorio y debe ser proporcionado por el usuario."
            )

        # Buscar documento existente con el mismo código
        existing_doc = Document.objects.filter(codigo=self.codigo).first()

        if existing_doc:
            # Si encontramos un documento existente, usamos su ID
            if not self.id_archivo:
                self.id_archivo = existing_doc.id_archivo

            # Eliminar el archivo anterior si se está actualizando
            if existing_doc.file and existing_doc.file != self.file:
                existing_doc.file.storage.delete(existing_doc.file.name)

            # Actualizar los campos del documento existente
            if existing_doc.id_archivo != self.id_archivo:
                existing_doc.delete()

        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        if self.file:
            self.file.storage.delete(self.file.name)
        super().delete(using, keep_parents)

    class Meta:
        unique_together = ["codigo"]


# Archivos globales caracterizacion REQUISITOS LEGALES Y NORMATIVOS ///////


class RequisitosLegalesNormativos_globales(Document):
    class Meta:
        db_table = (
            # REQUISITOS LEGALES Y NORMATIVOS
            "RequisitosLegalesNormativos_globales"  # Nombre de la tabla en la base de datos
        )


# Archivos globales caracterizacion REQUISITOS Y NECESIDADES DE LAS PARTES INTERESADAS ////////


class RequisitosNecesidadesPartesInteresadas_globales(Document):
    class Meta:
        db_table = (
            # REQUISITOS Y NECESIDADES DE LAS PARTES INTERESADAS
            "RequisitosNecesidadesPartesInteresadas_globales"  # Nombre de la tabla en la base de datos
        )


# Documentos asociados especificos caracterizacion ///////


class Document_admisiones_registro_control(Document):
    class Meta:
        db_table = (
            # DocumentosAsociados
            "document_admisiones_registro_control"  # Nombre de la tabla en la base de datos
        )


class Document_gestion_documental(Document):
    class Meta:
        db_table = "document_gestion_documental"


class Document_gestion_cartera(Document):
    class Meta:
        db_table = "document_gestion_cartera"


class Document_gestion_recursos_financieros(Document):
    class Meta:
        db_table = "document_gestion_recursos_financieros"


class Document_gestion_contractual(Document):
    class Meta:
        db_table = "document_gestion_contractual"


class Document_gestion_juridica(Document):
    class Meta:
        db_table = "document_gestion_juridica"


class Document_infraestructura_fisica(Document):
    class Meta:
        db_table = "document_infraestructura_fisica"


class Document_gestion_sistemas_comunicacion(Document):
    class Meta:
        db_table = "document_gestion_sistemas_comunicacion"


class Document_gestion_investigacion(Document):
    class Meta:
        db_table = "document_gestion_investigacion"


class Document_enseñanza_prendizaje_evaluacion(Document):
    class Meta:
        db_table = "document_enseñanza_prendizaje_evaluacion"


class Document_desarrollo_curricular(Document):
    class Meta:
        db_table = "document_desarrollo_curricular"


class Document_extension_proyeccion(Document):
    class Meta:
        db_table = "document_extension_proyeccion"


class Document_relacionamineto_egresados(Document):
    class Meta:
        db_table = "document_relacionamineto_egresados"


class Document_planeacion_estrategica_institucional(Document):
    class Meta:
        db_table = "document_planeacion_estrategica_institucional"


class Document_gestion_informacion(Document):
    class Meta:
        db_table = "document_gestion_informacion"


class Document_aseguramiento_calidad_academica(Document):
    class Meta:
        db_table = "document_aseguramiento_calidad_academica"


class Document_aseguramiento_calidad_procesos(Document):
    class Meta:
        db_table = "document_aseguramiento_calidad_procesos"


class Document_auditorias(Document):
    class Meta:
        db_table = "document_auditorias"


class Document_evaluacion_control(Document):
    class Meta:
        db_table = "document_evaluacion_control"


class Document_gestion_integrada(Document):
    class Meta:
        db_table = "document_gestion_integrada"


class Document_gestion_registro_calificado(Document):
    class Meta:
        db_table = "document_gestion_registro_calificado"


class Document_gestion_servicio_usuario(Document):
    class Meta:
        db_table = "document_gestion_servicio_usuario"


class Document_comunicacion(Document):
    class Meta:
        db_table = "document_comunicacion"


class Document_internacionalizacion(Document):
    class Meta:
        db_table = "document_internacionalizacion"


class Document_bienestar_institucional(Document):
    class Meta:
        db_table = "document_bienestar_institucional"


class Document_control_disciplinario(Document):
    class Meta:
        db_table = "document_control_disciplinario"


class Document_gestion_desarrollo_humano(Document):
    class Meta:
        db_table = "document_gestion_desarrollo_humano"


# Indicadores especificos caracterizacion /////


class Indicadores_admisiones_registro_control(Document):
    class Meta:
        db_table = (
            # Indicadores
            "Indicadores_admisiones_registro_control"  # Nombre de la tabla en la base de datos
        )


class Indicadores_gestion_documental(Document):
    class Meta:
        db_table = "Indicadores_gestion_documental"


class Indicadores_gestion_cartera(Document):
    class Meta:
        db_table = "Indicadores_gestion_cartera"


class Indicadores_gestion_recursos_financieros(Document):
    class Meta:
        db_table = "Indicadores_gestion_recursos_financieros"


class Indicadores_gestion_contractual(Document):
    class Meta:
        db_table = "Indicadores_gestion_contractual"


class Indicadores_gestion_juridica(Document):
    class Meta:
        db_table = "Indicadores_gestion_juridica"


class Indicadores_infraestructura_fisica(Document):
    class Meta:
        db_table = "Indicadores_infraestructura_fisica"


class Indicadores_gestion_sistemas_comunicacion(Document):
    class Meta:
        db_table = "Indicadores_gestion_sistemas_comunicacion"


class Indicadores_gestion_investigacion(Document):
    class Meta:
        db_table = "Indicadores_gestion_investigacion"


class Indicadores_enseñanza_prendizaje_evaluacion(Document):
    class Meta:
        db_table = "Indicadores_enseñanza_prendizaje_evaluacion"


class Indicadores_desarrollo_curricular(Document):
    class Meta:
        db_table = "Indicadores_desarrollo_curricular"


class Indicadores_extension_proyeccion(Document):
    class Meta:
        db_table = "Indicadores_extension_proyeccion"


class Indicadores_relacionamineto_egresados(Document):
    class Meta:
        db_table = "Indicadores_relacionamineto_egresados"


class Indicadores_planeacion_estrategica_institucional(Document):
    class Meta:
        db_table = "Indicadores_planeacion_estrategica_institucional"


class Indicadores_gestion_informacion(Document):
    class Meta:
        db_table = "Indicadores_gestion_informacion"


class Indicadores_aseguramiento_calidad_academica(Document):
    class Meta:
        db_table = "Indicadores_aseguramiento_calidad_academica"


class Indicadores_aseguramiento_calidad_procesos(Document):
    class Meta:
        db_table = "Indicadores_aseguramiento_calidad_procesos"


class Indicadores_auditorias(Document):
    class Meta:
        db_table = "Indicadores_auditorias"


class Indicadores_evaluacion_control(Document):
    class Meta:
        db_table = "Indicadores_evaluacion_control"


class Indicadores_gestion_integrada(Document):
    class Meta:
        db_table = "Indicadores_gestion_integrada"


class Indicadores_gestion_registro_calificado(Document):
    class Meta:
        db_table = "Indicadores_gestion_registro_calificado"


class Indicadores_gestion_servicio_usuario(Document):
    class Meta:
        db_table = "Indicadores_gestion_servicio_usuario"


class Indicadores_comunicacion(Document):
    class Meta:
        db_table = "Indicadores_comunicacion"


class Indicadores_internacionalizacion(Document):
    class Meta:
        db_table = "Indicadores_internacionalizacion"


class Indicadores_bienestar_institucional(Document):
    class Meta:
        db_table = "Indicadores_bienestar_institucional"


class Indicadores_control_disciplinario(Document):
    class Meta:
        db_table = "Indicadores_control_disciplinario"


class Indicadores_gestion_desarrollo_humano(Document):
    class Meta:
        db_table = "Indicadores_gestion_desarrollo_humano"


# modelos diagramas de procedimientos htmls ////////


class DiagramasProcedimientos(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(
        max_length=255, blank=True
    )  # Campo para almacenar el nombre

    def save(self, *args, **kwargs):
        # Obtiene la ruta sin la barra inicial y sin la extensión
        self.nombre = os.path.splitext(self.image.name)[0].lstrip(
            "/"
        )  # Elimina la barra inicial
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image ID: {self.id} uploaded at {self.uploaded_at}"


class DiPr_admisiones_registro_control(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_admisiones_registro_control"


class DiPr_gestion_documental(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_gestion_documental"


class DiPr_gestion_cartera(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_gestion_cartera"


class DiPr_gestion_recursos_financieros(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_gestion_recursos_financieros"


class DiPr_gestion_contractual(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_gestion_contractual"


class DiPr_gestion_juridica(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_gestion_juridica"


class DiPr_infraestructura_fisica(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_infraestructura_fisica"


class DiPr_gestion_sistemas_comunicacion(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_gestion_sistemas_comunicacion"


class DiPr_gestion_investigacion(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_gestion_investigacion"


class DiPr_enseñanza_prendizaje_evaluacion(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_enseñanza_prendizaje_evaluacion"


class DiPr_desarrollo_curricular(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_desarrollo_curricular"


class DiPr_extension_proyeccion(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_extension_proyeccion"


class DiPr_relacionamineto_egresados(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_relacionamineto_egresados"


class DiPr_planeacion_estrategica_institucional(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_planeacion_estrategica_institucional"


class DiPr_gestion_informacion(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_gestion_informacion"


class DiPr_aseguramiento_calidad_academica(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_aseguramiento_calidad_academica"


class DiPr_aseguramiento_calidad_procesos(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_aseguramiento_calidad_procesos"


class DiPr_auditorias(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_auditorias"


class DiPr_evaluacion_control(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_evaluacion_control"


class DiPr_gestion_integrada(DiagramasProcedimientos):
    class Meta:
        db_table = "gestion_integrada"


class DiPr_gestion_registro_calificado(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_gestion_registro_calificado"


class DiPr_gestion_servicio_usuario(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_gestion_servicio_usuario"


class DiPr_comunicacion(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_comunicacion"


class DiPr_internacionalizacion(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_internacionalizacion"


class DiPr_bienestar_institucional(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_bienestar_institucional"


class DiPr_control_disciplinario(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_control_disciplinario"


class DiPr_gestion_desarrollo_humano(DiagramasProcedimientos):
    class Meta:
        db_table = "DiPr_gestion_desarrollo_humano"
