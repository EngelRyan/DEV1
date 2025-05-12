from django.urls import path
from .views.estaticas import *

app_name = 'aula'

urlpatterns = [
    path('funcao/teste', primeira_view, name="primeira_view"),
    path('classe/teste', PrimeiraView.as_view(), name="primeira_view_classe"),
    path('funcao/saudacao', saudacao, name="saudacao")
]