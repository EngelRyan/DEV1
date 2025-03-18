from django.db import models
from django.utils.translation import gettext_lazy as _

class TipoMarca(models.TextChoices):
    M_100 = "100M", _("100 metros")
    M_400 = "400M", _("400 metros")
    KM_1 = "1KM", _("1 Quilômetro")
    KM_5 = "5KM", _("5 Quilômetros")
    KM_10 = "10KM", _("10 Quilômetros")
    KM_15 = "15KM", _("15 Quilômetros")
    KM_20 = "20KM", _("20 Quilômetros")
    MEIA_MARATONA = "MEIA", _("Meia Maratona")
    KM_30 = "30KM", _("30 Quilômetros")
    MARATONA = "MARATONA", _("Maratona")
    LONGA_DISTANCIA = "LONGA_DISTANCIA", _("Maior distância")
    LONGA_DURACAO = "LONGA_DURACAO", _("Maior duração")