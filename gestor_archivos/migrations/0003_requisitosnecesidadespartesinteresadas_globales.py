# Generated by Django 5.1.4 on 2025-02-10 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_archivos', '0002_requisitoslegalesnormativos_globales_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequisitosNecesidadesPartesInteresadas_globales',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestor_archivos.document')),
            ],
            options={
                'db_table': 'RequisitosNecesidadesPartesInteresadas_globales',
            },
            bases=('gestor_archivos.document',),
        ),
    ]
