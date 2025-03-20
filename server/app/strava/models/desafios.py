from django.core.validators import MinLengthValidator
from .base_model import BaseModel
from django.db import models
from ..enumerations.tipo_esporte import TipoEsporte

class Desafio(BaseModel):
    nome = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    data_inicio = models.DateField()
    data_fim = models.DateField()
    tipo_esporte = models.CharField(choices=TipoEsporte, max_length=50)
    visao_geral = models.TextField()
    selo = models.CharField(max_length=5)

    def str(self):
        return self.nome