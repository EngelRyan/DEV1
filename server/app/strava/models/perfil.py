from django.db import models
from .base_model import BaseModel
from strava.enumerations.genero import Genero

class Perfil(BaseModel):
    email = models.EmailField(max_length=100)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    senha = models.CharField(max_length=25)
    data_nascimento = models.DateField()
    local = models.CharField(max_length=100)
    genero = models.CharField(max_length=20, choices=Genero.choices)
    peso_ideal = models.FloatField()
    biografia_texto = models.TextField(blank=True, null=True)
    premium_tool = models.BooleanField(default=False)
    membro_desde = models.DateField(auto_now_add=True)

    def __str__(self):
        return f' {self.nome} || {self.email}'