# Generated by Django 5.1.6 on 2025-03-25 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0006_magazine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='name',
            field=models.CharField(help_text='...', max_length=15, verbose_name='Name'),
        ),
    ]
