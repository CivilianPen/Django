# Generated by Django 5.0.2 on 2024-02-22 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='Language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.lang'),
        ),
    ]
