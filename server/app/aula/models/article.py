from django.core.validators import MinValueValidator, MaxValueValidator
from .base_model import BaseModel
from django.db import models

from .reporter import Reporter


class Article(BaseModel):

    title = models.CharField( max_length=100, null=False, blank=False, help_text="...", verbose_name="Title")
    pub_date = models.DateField(verbose_name="Publish Date")
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, verbose_name="Reporter")

    def __str__(self):
        return f'{self.title} | Published by {self.reporter.name}'
