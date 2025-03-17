# Generated by Django 5.0 on 2025-03-17 22:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome para a tag, entre 5 e 200 caracteres.', max_length=200, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Descrição')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
