from django.db import models
from .base_model import BaseModel

from strava.enumerations.tipo_esporte import TipoEsporte

class Atividade(BaseModel):
    nome = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True, null=True)
    data = models.DateField()
    tipo_esporte = models.CharField(max_length=20, choices=TipoEsporte.choices)
    inicio_tempo = models.TimeField()
    duracao_tempo = models.TimeField()
    distancia_float = models.FloatField()
    ritmo_int_min_value_0 = models.IntegerField(default=0)
    elevacao_total_int_min_value_0 = models.IntegerField(default=0)


    def __str__(self):
        return self.nome