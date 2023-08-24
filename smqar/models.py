from django.db import models
from django.db.models import PositiveSmallIntegerField
# Create your models here.
class Concentracao(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField()
    c_mp10 = models.FloatField()
    c_mp25 = models.FloatField()

    def __str__(self):
        return str(self.data)
class Indice(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    indice_mp25 = models.FloatField()
    indice_mp10 = models.FloatField()
    classificacao = PositiveSmallIntegerField()

    def __str__(self):
        return str(self.data)
