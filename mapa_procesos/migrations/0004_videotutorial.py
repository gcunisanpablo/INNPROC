# Generated by Django 5.1.4 on 2025-02-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa_procesos', '0003_ec_evaluacion_control'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoTutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('icon_class', models.CharField(max_length=50)),
                ('video_id', models.CharField(max_length=20)),
            ],
        ),
    ]
