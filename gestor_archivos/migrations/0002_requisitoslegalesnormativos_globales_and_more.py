# Generated by Django 5.1.4 on 2025-02-07 14:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_archivos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequisitosLegalesNormativos_globales',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestor_archivos.document')),
            ],
            options={
                'db_table': 'RequisitosLegalesNormativos_globales',
            },
            bases=('gestor_archivos.document',),
        ),
        migrations.AlterField(
            model_name='document',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
