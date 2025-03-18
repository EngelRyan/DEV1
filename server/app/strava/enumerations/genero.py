from django.db import models
from django.utils.translation import gettext_lazy as _

class Genero(models.TextChoices):
    MAN = "MAN", _("Homem")
    WOMAN = "WOMAN", _("Mulher")
    NON_BINARY = "NON_BINARY", _("Não binário")
    NOT_INFORMED = "NOT_INFORMED", _("Não informado")