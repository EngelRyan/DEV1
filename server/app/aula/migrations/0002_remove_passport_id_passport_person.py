# Generated by Django 5.0 on 2025-03-24 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passport',
            name='id',
        ),
        migrations.AddField(
            model_name='passport',
            name='person',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='aula.person'),
            preserve_default=False,
        ),
    ]
