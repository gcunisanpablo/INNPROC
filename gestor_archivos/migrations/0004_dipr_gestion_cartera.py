# Generated by Django 5.1.4 on 2025-02-12 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_archivos', '0003_requisitosnecesidadespartesinteresadas_globales'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiPr_gestion_cartera',
            fields=[
                ('diagramasprocedimientos_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestor_archivos.diagramasprocedimientos')),
            ],
            options={
                'db_table': 'DiPr_gestion_cartera',
            },
            bases=('gestor_archivos.diagramasprocedimientos',),
        ),
    ]
