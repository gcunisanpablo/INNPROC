from django import forms
from gestor_archivos.models import (
    # Modelos Padres
    Document,
    DiagramasProcedimientos,
    # Globales
    RequisitosLegalesNormativos_globales,
    RequisitosNecesidadesPartesInteresadas_globales,
    # Documentos asociados
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
    # Diagramas procedimientos
    DiPr_admisiones_registro_control,
    DiPr_gestion_documental,
    DiPr_gestion_cartera,
    DiPr_gestion_recursos_financieros,
    DiPr_gestion_contractual,
    DiPr_gestion_juridica,
    DiPr_infraestructura_fisica,
    DiPr_gestion_sistemas_comunicacion,
    DiPr_gestion_investigacion,
    DiPr_enseñanza_prendizaje_evaluacion,
    DiPr_desarrollo_curricular,
    DiPr_extension_proyeccion,
    DiPr_relacionamineto_egresados,
    DiPr_planeacion_estrategica_institucional,
    DiPr_gestion_informacion,
    DiPr_aseguramiento_calidad_academica,
    DiPr_aseguramiento_calidad_procesos,
    DiPr_auditorias,
    DiPr_evaluacion_control,
    DiPr_gestion_integrada,
    DiPr_gestion_registro_calificado,
    DiPr_gestion_servicio_usuario,
    DiPr_comunicacion,
    DiPr_internacionalizacion,
    DiPr_bienestar_institucional,
    DiPr_control_disciplinario,
    DiPr_gestion_desarrollo_humano,
    # Indicadores
    Indicadores_admisiones_registro_control,
    Indicadores_gestion_documental,
    Indicadores_gestion_cartera,
    Indicadores_gestion_recursos_financieros,
    Indicadores_gestion_contractual,
    Indicadores_gestion_juridica,
    Indicadores_infraestructura_fisica,
    Indicadores_gestion_sistemas_comunicacion,
    Indicadores_gestion_investigacion,
    Indicadores_enseñanza_prendizaje_evaluacion,
    Indicadores_desarrollo_curricular,
    Indicadores_extension_proyeccion,
    Indicadores_relacionamineto_egresados,
    Indicadores_planeacion_estrategica_institucional,
    Indicadores_gestion_informacion,
    Indicadores_aseguramiento_calidad_academica,
    Indicadores_aseguramiento_calidad_procesos,
    Indicadores_auditorias,
    Indicadores_evaluacion_control,
    Indicadores_gestion_integrada,
    Indicadores_gestion_registro_calificado,
    Indicadores_gestion_servicio_usuario,
    Indicadores_comunicacion,
    Indicadores_internacionalizacion,
    Indicadores_bienestar_institucional,
    Indicadores_control_disciplinario,
    Indicadores_gestion_desarrollo_humano,
)

# Documentos htmls modelos ///////////////


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["codigo", "caracterizacion", "titulo", "file"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Asegurarse de que los campos sean obligatorios
        self.fields["codigo"].required = True
        self.fields["titulo"].required = True
        self.fields["file"].required = True

        # Cambia a CharField con un widget de texto
        self.fields["caracterizacion"] = forms.CharField(
            widget=forms.TextInput(attrs={"class": "form-control"}),
            label="caracterizacion",
        )


# Archivos globales caracterizacion REQUISITOS LEGALES Y NORMATIVOS ///////


class RequisitosLegalesNormativos_globales(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = RequisitosLegalesNormativos_globales  # Especifica el nuevo modelo
        fields = (
            DocumentForm.Meta.fields
        )  # Usa los mismos campos que el formulario base

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Archivos globales caracterizacion REQUISITOS Y NECESIDADES DE LAS PARTES INTERESADAS ////////


class RequisitosNecesidadesPartesInteresadas_globales(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = RequisitosNecesidadesPartesInteresadas_globales  # Especifica el nuevo modelo
        fields = (
            DocumentForm.Meta.fields
        )  # Usa los mismos campos que el formulario base

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Documentos asociados especificos caracterizacion //////


class Document_admisiones_registro_control(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_admisiones_registro_control  # Especifica el nuevo modelo
        fields = (
            DocumentForm.Meta.fields
        )  # Usa los mismos campos que el formulario base

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_gestion_documental(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_gestion_documental
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_gestion_cartera(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_gestion_cartera
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_gestion_recursos_financieros(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_gestion_recursos_financieros
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_gestion_contractual(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_gestion_contractual
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_gestion_juridica(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_gestion_juridica
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_infraestructura_fisica(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_infraestructura_fisica
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_gestion_sistemas_comunicacion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_gestion_sistemas_comunicacion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_gestion_investigacion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_gestion_investigacion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_enseñanza_prendizaje_evaluacion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_enseñanza_prendizaje_evaluacion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_desarrollo_curricular(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_desarrollo_curricular
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_extension_proyeccion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_extension_proyeccion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_relacionamineto_egresados(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_relacionamineto_egresados
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_planeacion_estrategica_institucional(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_planeacion_estrategica_institucional
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_gestion_informacion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_gestion_informacion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_aseguramiento_calidad_academica(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_aseguramiento_calidad_academica
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_aseguramiento_calidad_procesos(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_aseguramiento_calidad_procesos
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_auditorias(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_auditorias
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_evaluacion_control(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_evaluacion_control
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_gestion_integrada(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_gestion_integrada
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_gestion_registro_calificado(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_gestion_registro_calificado
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_gestion_servicio_usuario(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_gestion_servicio_usuario
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_comunicacion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_comunicacion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_internacionalizacion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_internacionalizacion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_bienestar_institucional(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_bienestar_institucional
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_control_disciplinario(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_control_disciplinario
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Document_gestion_desarrollo_humano(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Document_gestion_desarrollo_humano
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# indicadores especificos caracterrizacion //////


class Indicadores_admisiones_registro_control(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_admisiones_registro_control  # Especifica el nuevo modelo
        fields = (
            DocumentForm.Meta.fields
        )  # Usa los mismos campos que el formulario base

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_gestion_documental(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_gestion_documental
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_gestion_cartera(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_gestion_cartera
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_gestion_recursos_financieros(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_gestion_recursos_financieros
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_gestion_contractual(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_gestion_contractual
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_gestion_juridica(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_gestion_juridica
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_infraestructura_fisica(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_infraestructura_fisica
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_gestion_sistemas_comunicacion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_gestion_sistemas_comunicacion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_gestion_investigacion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_gestion_investigacion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_enseñanza_prendizaje_evaluacion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_enseñanza_prendizaje_evaluacion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_desarrollo_curricular(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_desarrollo_curricular
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_extension_proyeccion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_extension_proyeccion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_relacionamineto_egresados(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_relacionamineto_egresados
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_planeacion_estrategica_institucional(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_planeacion_estrategica_institucional
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_gestion_informacion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_gestion_informacion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_aseguramiento_calidad_academica(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_aseguramiento_calidad_academica
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_aseguramiento_calidad_procesos(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_aseguramiento_calidad_procesos
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_auditorias(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_auditorias
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_evaluacion_control(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_evaluacion_control
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_gestion_integrada(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_gestion_integrada
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_gestion_registro_calificado(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_gestion_registro_calificado
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_gestion_servicio_usuario(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_gestion_servicio_usuario
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_comunicacion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_comunicacion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_internacionalizacion(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_internacionalizacion
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_bienestar_institucional(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_bienestar_institucional
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_control_disciplinario(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_control_disciplinario
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Indicadores_gestion_desarrollo_humano(DocumentForm):
    class Meta(DocumentForm.Meta):
        model = Indicadores_gestion_desarrollo_humano
        fields = DocumentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Diagramas de procedimientos htmls /////////////////


class DiagramasProcedimientos(forms.ModelForm):
    class Meta:
        model = DiagramasProcedimientos
        fields = ["image"]  # Solo incluimos el campo de la imagen

        widgets = {
            "image": forms.ClearableFileInput(
                attrs={"class": "form-control", "required": True}
            ),
        }

        labels = {
            "image": "Cargar Imagen",
        }


class DiPr_admisiones_registro_control_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_admisiones_registro_control  # Se especifica el nuevo modelo
        fields = (
            DiagramasProcedimientos.Meta.fields
        )  # mismos campos del formulario base

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_gestion_documental_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_gestion_documental
        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_gestion_cartera_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_gestion_cartera
        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_gestion_recursos_financieros_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_gestion_recursos_financieros
        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_gestion_contractual_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_gestion_contractual
        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_gestion_juridica_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_gestion_juridica
        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_infraestructura_fisica_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_infraestructura_fisica
        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_gestion_sistemas_comunicacion_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_gestion_sistemas_comunicacion
        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_gestion_investigacion_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_gestion_investigacion
        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_enseñanza_prendizaje_evaluacion_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_enseñanza_prendizaje_evaluacion

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_desarrollo_curricular_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_desarrollo_curricular

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_extension_proyeccion_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_extension_proyeccion

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_relacionamineto_egresados_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_relacionamineto_egresados

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_planeacion_estrategica_institucional_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_planeacion_estrategica_institucional

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_gestion_informacion_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_gestion_informacion

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_aseguramiento_calidad_academica_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_aseguramiento_calidad_academica

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_aseguramiento_calidad_procesos_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_aseguramiento_calidad_procesos

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_auditorias_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_auditorias

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_evaluacion_control_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_evaluacion_control

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_gestion_integrada_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_gestion_integrada

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_gestion_registro_calificado_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_gestion_registro_calificado

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_gestion_servicio_usuario_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_gestion_servicio_usuario

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_comunicacion_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_comunicacion

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_internacionalizacion_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_internacionalizacion

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_bienestar_institucional_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_bienestar_institucional

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_control_disciplinario_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_control_disciplinario

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiPr_gestion_desarrollo_humano_form(DiagramasProcedimientos):
    class Meta(DiagramasProcedimientos.Meta):
        model = DiPr_gestion_desarrollo_humano

        fields = DiagramasProcedimientos.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
