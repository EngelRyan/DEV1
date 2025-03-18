from django.db import models
from django.utils.translation import gettext_lazy as _

class TipoEsporte(models.TextChoices):
    RUN = "RUN", _("Corrida")
    TRAIL_RUN = "TRAIL_RUN", _("Corrida de Trilhas")
    BIKE = "BIKE", _("Treino de Bicicleta")
    WALK = "WALK", _("Caminhada")
    HIIT = "HIIT", _("Treino de Alta Intensidade")
    STRENGTH = "STRENGTH", _("Treino de Força")
    CARDIO = "CARDIO", _("Treino Aeróbico")
    SWIMMING = "SWIMMING", _("Natação")