from django import forms
from .models import (
    # base formatos
    DocumentFormatosAsociados,
    # base diagramas de flujo (image)
    DocumentAsociadosDiagramasFlujo,
    # MODELOS
    # diagramas
    DocumentImage_admisiones_registro_control,
    DocumentImage_gestion_documental,
    DocumentImage_gestion_cartera,
    DocumentImage_gestion_recursos_financieros,
    DocumentImage_gestion_contractual,
    DocumentImage_gestion_juridica,
    DocumentImage_infraestructura_fisica,
    DocumentImage_gestion_sistemas_comunicacion,
    DocumentImage_gestion_investigacion,
    DocumentImage_enseñanza_prendizaje_evaluacion,
    DocumentImage_desarrollo_curricular,
    DocumentImage_extension_proyeccion,
    DocumentImage_relacionamineto_egresados,
    DocumentImage_planeacion_estrategica_institucional,
    DocumentImage_gestion_informacion,
    DocumentImage_aseguramiento_calidad_academica,
    DocumentImage_aseguramiento_calidad_procesos,
    DocumentImage_auditorias,
    DocumentImage_evaluacion_control,
    DocumentImage_gestion_integrada,
    DocumentImage_gestion_registro_calificado,
    DocumentImage_gestion_servicio_usuario,
    DocumentImage_comunicacion,
    DocumentImage_internacionalizacion,
    DocumentImage_bienestar_institucional,
    DocumentImage_control_disciplinario,
    DocumentImage_gestion_desarrollo_humano,
    # formatos
    DocumentDoAs_admisiones_registro_control_FoAs,
    DocumentDoAs_gestion_documental_FoAs,
    DocumentDoAs_gestion_cartera_FoAs,
    DocumentDoAs_gestion_recursos_financieros_FoAs,
    DocumentDoAs_gestion_contractual_FoAs,
    DocumentDoAs_gestion_juridica_FoAs,
    DocumentDoAs_infraestructura_fisica_FoAs,
    DocumentDoAs_gestion_sistemas_comunicacion_FoAs,
    DocumentDoAs_gestion_investigacion_FoAs,
    DocumentDoAs_enseñanza_prendizaje_evaluacion_FoAs,
    DocumentDoAs_desarrollo_curricular_FoAs,
    DocumentDoAs_extension_proyeccion_FoAs,
    DocumentDoAs_relacionamineto_egresados_FoAs,
    DocumentDoAs_planeacion_estrategica_institucional_FoAs,
    DocumentDoAs_gestion_informacion_FoAs,
    DocumentDoAs_aseguramiento_calidad_academica_FoAs,
    DocumentDoAs_aseguramiento_calidad_procesos_FoAs,
    DocumentDoAs_auditorias_FoAs,
    DocumentDoAs_evaluacion_control_FoAs,
    DocumentDoAs_gestion_integrada_FoAs,
    DocumentDoAs_gestion_registro_calificado_FoAs,
    DocumentDoAs_gestion_servicio_usuario_FoAs,
    DocumentDoAs_comunicacion_FoAs,
    DocumentDoAs_internacionalizacion_FoAs,
    DocumentDoAs_bienestar_institucional_FoAs,
    DocumentDoAs_control_disciplinario_FoAs,
    DocumentDoAs_gestion_desarrollo_humano_FoAs,
)


# Documentos asociadas diagramas
class DocumentImageAsociada(forms.ModelForm):
    class Meta:
        model = DocumentAsociadosDiagramasFlujo
        fields = ["image"]


# Diagramas asociados a documentos asociados especificos de caracterizacion//////


class DocumentImage_admisiones_registro_control(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_admisiones_registro_control  # Especifica el nuevo modelo
        fields = (
            DocumentImageAsociada.Meta.fields
        )  # Usa los mismos campos que el formulario base

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_gestion_documental(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_gestion_documental
        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_gestion_cartera(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_gestion_cartera
        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_gestion_recursos_financieros(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_gestion_recursos_financieros
        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_gestion_contractual(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_gestion_contractual
        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_gestion_juridica(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_gestion_juridica
        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_infraestructura_fisica(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_infraestructura_fisica
        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_gestion_sistemas_comunicacion(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_gestion_sistemas_comunicacion
        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_gestion_investigacion(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_gestion_investigacion

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_enseñanza_prendizaje_evaluacion(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_enseñanza_prendizaje_evaluacion

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_desarrollo_curricular(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_desarrollo_curricular

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_extension_proyeccion(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_extension_proyeccion

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_relacionamineto_egresados(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_relacionamineto_egresados

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_planeacion_estrategica_institucional(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_planeacion_estrategica_institucional

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_gestion_informacion(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_gestion_informacion

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_aseguramiento_calidad_academica(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_aseguramiento_calidad_academica

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_aseguramiento_calidad_procesos(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_aseguramiento_calidad_procesos

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_auditorias(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_auditorias

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_evaluacion_control(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_evaluacion_control

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_gestion_integrada(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_gestion_integrada

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_gestion_registro_calificado(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_gestion_registro_calificado

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_gestion_servicio_usuario(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_gestion_servicio_usuario

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_comunicacion(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_comunicacion

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_internacionalizacion(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_internacionalizacion

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_bienestar_institucional(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_bienestar_institucional

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_control_disciplinario(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_control_disciplinario

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentImage_gestion_desarrollo_humano(DocumentImageAsociada):
    class Meta(DocumentImageAsociada.Meta):
        model = DocumentImage_gestion_desarrollo_humano

        fields = DocumentImageAsociada.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Modelo para formatos de documetos asociados


class DocumentFormatosAsociados(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()

        # Depuración de campos
        for field, value in cleaned_data.items():
            print(f"Campo {field}: {value}")

        # Validaciones adicionales
        if not cleaned_data.get("title"):
            self.add_error("title", "El título es obligatorio")

        if not cleaned_data.get("codigo"):
            self.add_error("codigo", "El código es obligatorio")

        return cleaned_data

    class Meta:
        model = DocumentFormatosAsociados
        fields = ["title", "codigo", "caracterizacion", "procedimiento", "file"]


# Formatos asociados a documentos asociados especificos de caracterizacion ////////


class DocumentDoAs_admisiones_registro_control_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = (
            DocumentDoAs_admisiones_registro_control_FoAs  # Especifica el nuevo modelo
        )
        fields = (
            DocumentFormatosAsociados.Meta.fields
        )  # Usa los mismos campos que el formulario base

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_gestion_documental_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_gestion_documental_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_gestion_cartera_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_gestion_cartera_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_gestion_recursos_financieros_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_gestion_recursos_financieros_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_gestion_contractual_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_gestion_contractual_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_gestion_juridica_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_gestion_juridica_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_infraestructura_fisica_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_infraestructura_fisica_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_gestion_sistemas_comunicacion_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_gestion_sistemas_comunicacion_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_gestion_investigacion_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_gestion_investigacion_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_enseñanza_prendizaje_evaluacion_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_enseñanza_prendizaje_evaluacion_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_desarrollo_curricular_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_desarrollo_curricular_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_extension_proyeccion_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_extension_proyeccion_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_relacionamineto_egresados_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_relacionamineto_egresados_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_planeacion_estrategica_institucional_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_planeacion_estrategica_institucional_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_gestion_informacion_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_gestion_informacion_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_aseguramiento_calidad_academica_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_aseguramiento_calidad_academica_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_aseguramiento_calidad_procesos_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_aseguramiento_calidad_procesos_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_auditorias_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_auditorias_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_evaluacion_control_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_evaluacion_control_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_gestion_integrada_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_gestion_integrada_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_gestion_registro_calificado_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_gestion_registro_calificado_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_gestion_servicio_usuario_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_gestion_servicio_usuario_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_comunicacion_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_comunicacion_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_internacionalizacion_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_internacionalizacion_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_bienestar_institucional_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_bienestar_institucional_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_control_disciplinario_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_control_disciplinario_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DocumentDoAs_gestion_desarrollo_humano_FoAs(DocumentFormatosAsociados):
    class Meta(DocumentFormatosAsociados.Meta):
        model = DocumentDoAs_gestion_desarrollo_humano_FoAs
        fields = DocumentFormatosAsociados.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
