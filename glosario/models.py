from django.db import models


class Glosario(models.Model):
    id_termino = models.AutoField(primary_key=True)
    termino = models.CharField(max_length=150, verbose_name="termino")
    definicion = models.TextField(max_length=2000, verbose_name="definicion")
