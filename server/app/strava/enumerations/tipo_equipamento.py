from django.db import models
from django.utils.translation import gettext_lazy as _

class TipoEquipamento(models.TextChoices):
    SNEAKER = "SNEAKER", _("Tênis")
    BIKE = "BIKE", _("Bicicleta")
    SMART_DEVICE = "SMART_DEVICE", _("Dispositivo Inteligente")