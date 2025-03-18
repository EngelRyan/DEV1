from django.db import models
from .base_model import BaseModel

from strava.enumerations.tipo_marca import TipoMarca
from strava.enumerations.tipo_esporte import TipoEsporte


class Record(BaseModel):
    nome = models.CharField(max_length=20)
    tipo_marca = models.CharField(max_length=20, choices=TipoMarca.choices)
    tipo_esporte = models.CharField(max_length=20, choices=TipoEsporte.choices)
    ritmo = models.TimeField()
    duracao = models.TimeField()


    def __str__(self):
        return self.nome