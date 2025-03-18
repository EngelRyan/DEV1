from django.db import models
from .base_model import BaseModel

from strava.enumerations.tipo_esporte import TipoEsporte

class Clube(BaseModel):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    pais_origem = models.CharField(max_length=100)
    tipo_esporte_clube = models.CharField(max_length=50, choices=TipoEsporte.choices)

    def __str__(self):
        return self.nome