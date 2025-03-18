from django.db import models
from .base_model import BaseModel

from strava.enumerations.tipo_equipamento import TipoEquipamento

# Model Equipamento
class Equipamento(BaseModel):
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo_string_2_50 = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50, blank=True, null=True)
    tipo_equipamento = models.CharField(max_length=20, choices=TipoEquipamento)


    def __str__(self):
        return self.nome