# Generated by Django 5.1.4 on 2025-02-17 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_archivos', '0006_dipr_evaluacion_control_document_evaluacion_control_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiPr_gestion_integrada',
            fields=[
                ('diagramasprocedimientos_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestor_archivos.diagramasprocedimientos')),
            ],
            options={
                'db_table': 'gestion_integrada',
            },
            bases=('gestor_archivos.diagramasprocedimientos',),
        ),
        migrations.CreateModel(
            name='Document_gestion_integrada',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestor_archivos.document')),
            ],
            options={
                'db_table': 'document_gestion_integrada',
            },
            bases=('gestor_archivos.document',),
        ),
        migrations.CreateModel(
            name='Indicadores_gestion_integrada',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestor_archivos.document')),
            ],
            options={
                'db_table': 'Indicadores_gestion_integrada',
            },
            bases=('gestor_archivos.document',),
        ),
    ]
