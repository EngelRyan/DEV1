# Generated by Django 5.0 on 2025-03-24 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='...', max_length=50, verbose_name='Number')),
                ('issue_date', models.DateField(verbose_name='Issue Date')),
                ('expiration', models.DateField(verbose_name='Expiration')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='...', max_length=50, verbose_name='Name')),
                ('bith_date', models.DateField(verbose_name='Birth Date')),
                ('cpf', models.CharField(help_text='Valid CPF...', max_length=11, verbose_name='CPF')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
