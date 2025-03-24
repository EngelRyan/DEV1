from django.core.validators import MinValueValidator, MaxValueValidator
from .base_model import BaseModel
from django.db import models

class Person(BaseModel):

    name = models.CharField( max_length=50, null=False, blank=False, help_text="...", verbose_name="Name")
    bith_date = models.DateField(verbose_name="Birth Date")
    cpf = models.CharField(max_length=11, null=False, blank=False, help_text="Valid CPF...", verbose_name="CPF")

    def __str__(self):
        return f'{self.name} | {self.cpf} '