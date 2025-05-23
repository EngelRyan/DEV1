# Generated by Django 5.1.6 on 2025-03-20 00:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('data', models.DateField()),
                ('tipo_esporte', models.CharField(choices=[('RUN', 'Corrida'), ('TRAIL_RUN', 'Corrida de Trilhas'), ('BIKE', 'Treino de Bicicleta'), ('WALK', 'Caminhada'), ('HIIT', 'Treino de Alta Intensidade'), ('STRENGTH', 'Treino de Força'), ('CARDIO', 'Treino Aeróbico'), ('SWIMMING', 'Natação')], max_length=20)),
                ('inicio_tempo', models.TimeField()),
                ('duracao_tempo', models.TimeField()),
                ('distancia_float', models.FloatField()),
                ('ritmo_int_min_value_0', models.IntegerField(default=0)),
                ('elevacao_total_int_min_value_0', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('pais_origem', models.CharField(max_length=100)),
                ('tipo_esporte_clube', models.CharField(choices=[('RUN', 'Corrida'), ('TRAIL_RUN', 'Corrida de Trilhas'), ('BIKE', 'Treino de Bicicleta'), ('WALK', 'Caminhada'), ('HIIT', 'Treino de Alta Intensidade'), ('STRENGTH', 'Treino de Força'), ('CARDIO', 'Treino Aeróbico'), ('SWIMMING', 'Natação')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Desafio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)])),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('tipo_esporte', models.CharField(choices=[('RUN', 'Corrida'), ('TRAIL_RUN', 'Corrida de Trilhas'), ('BIKE', 'Treino de Bicicleta'), ('WALK', 'Caminhada'), ('HIIT', 'Treino de Alta Intensidade'), ('STRENGTH', 'Treino de Força'), ('CARDIO', 'Treino Aeróbico'), ('SWIMMING', 'Natação')], max_length=50)),
                ('visao_geral', models.TextField()),
                ('selo', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo_string_2_50', models.CharField(max_length=50)),
                ('apelido', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo_equipamento', models.CharField(choices=[('SNEAKER', 'Tênis'), ('BIKE', 'Bicicleta'), ('SMART_DEVICE', 'Dispositivo Inteligente')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('senha', models.CharField(max_length=25)),
                ('data_nascimento', models.DateField()),
                ('local', models.CharField(max_length=100)),
                ('genero', models.CharField(choices=[('MAN', 'Homem'), ('WOMAN', 'Mulher'), ('NON_BINARY', 'Não binário'), ('NOT_INFORMED', 'Não informado')], max_length=20)),
                ('peso_ideal', models.FloatField()),
                ('biografia_texto', models.TextField(blank=True, null=True)),
                ('premium_tool', models.BooleanField(default=False)),
                ('membro_desde', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('tipo_marca', models.CharField(choices=[('100M', '100 metros'), ('400M', '400 metros'), ('1KM', '1 Quilômetro'), ('5KM', '5 Quilômetros'), ('10KM', '10 Quilômetros'), ('15KM', '15 Quilômetros'), ('20KM', '20 Quilômetros'), ('MEIA', 'Meia Maratona'), ('30KM', '30 Quilômetros'), ('MARATONA', 'Maratona'), ('LONGA_DISTANCIA', 'Maior distância'), ('LONGA_DURACAO', 'Maior duração')], max_length=20)),
                ('tipo_esporte', models.CharField(choices=[('RUN', 'Corrida'), ('TRAIL_RUN', 'Corrida de Trilhas'), ('BIKE', 'Treino de Bicicleta'), ('WALK', 'Caminhada'), ('HIIT', 'Treino de Alta Intensidade'), ('STRENGTH', 'Treino de Força'), ('CARDIO', 'Treino Aeróbico'), ('SWIMMING', 'Natação')], max_length=20)),
                ('ritmo', models.TimeField()),
                ('duracao', models.TimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
