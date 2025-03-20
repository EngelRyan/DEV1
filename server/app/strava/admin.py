from django.contrib import admin
from .models.atividade import *
from .models.clube import *
from .models.desafios import *
from .models.equipamento import *
from .models.perfil import *
from .models.record import *

admin.site.register(Atividade)
admin.site.register(Clube)
admin.site.register(Desafio)
admin.site.register(Equipamento)
admin.site.register(Perfil)
admin.site.register(Record)
