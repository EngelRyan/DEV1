from django.core.validators import MinValueValidator, MaxValueValidator
from .base_model import BaseModel
from django.db import models

from .person import Person


class Passport(BaseModel):

    number = models.CharField( max_length=15, null=False, blank=False, help_text="...", verbose_name="Number")
    issue_date = models.DateField(verbose_name="Issue Date")
    expiration = models.DateField(verbose_name="Expiration")
    owner = models.OneToOneField(Person, on_delete=models.CASCADE , primary_key=True,verbose_name="Owner")

    def __str__(self):
        return f'{self.number} | Owner: {self.owner.name}'
