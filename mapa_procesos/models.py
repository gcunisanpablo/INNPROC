from django.db import models


class VideoTutorial(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    icon_class = models.CharField(max_length=50, verbose_name="Clase del ícono")
    video_id = models.CharField(max_length=20, verbose_name="ID del Video")

    class Meta:
        verbose_name = "Tutorial"
        verbose_name_plural = "Tutoriales"

    def __str__(self):
        return self.title


# EditableContent admisiones_registro_control
class EC_admisiones_registro_control(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_gestion_documental(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_gestion_cartera(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_gestion_recursos_financieros(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_gestion_contractual(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_gestion_juridica(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_infraestructura_fisica(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_gestion_sistemas_comunicacion(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_gestion_investigacion(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_enseñanza_prendizaje_evaluacion(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_desarrollo_curricular(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_extension_proyeccion(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_relacionamineto_egresados(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_planeacion_estrategica_institucional(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_gestion_informacion(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_aseguramiento_calidad_academica(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_aseguramiento_calidad_procesos(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_auditorias(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_evaluacion_control(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_gestion_integrada(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_gestion_registro_calificado(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_gestion_servicio_usuario(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_comunicacion(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_internacionalizacion(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_bienestar_institucional(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_control_disciplinario(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier


class EC_gestion_desarrollo_humano(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.identifier
