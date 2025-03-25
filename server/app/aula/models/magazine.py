from django.core.validators import MinValueValidator, MaxValueValidator
from .base_model import BaseModel
from django.db import models

from .article import Article


class Magazine(BaseModel):

    name = models.CharField( max_length=100, null=False, blank=False, help_text="...", verbose_name="Name")
    edition = models.DateField(verbose_name="Edition")
    article = models.ManyToManyField(Article, verbose_name="Articles")

    def __str__(self):
        articles = ", ".join(article.title for article in self.article.all())
        return f'{self.name} | {articles}'
