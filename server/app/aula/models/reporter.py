from django.core.validators import MinValueValidator, MaxValueValidator
from .base_model import BaseModel
from django.db import models



class Reporter(BaseModel):


    name = models.CharField( max_length=50, null=False, blank=False, help_text="...", verbose_name="Name")
    email = models.EmailField(help_text="#####@mail.com", verbose_name="Email")
    cpf = models.CharField(max_length=11, null=False, blank=False, help_text="Valid CPF...", verbose_name="CPF")

    def __str__(self):
        return f'{self.name} | Contact: {self.email}'