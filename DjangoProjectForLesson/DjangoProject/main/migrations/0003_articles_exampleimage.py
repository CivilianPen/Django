# Generated by Django 5.0.2 on 2024-02-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_articles_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='ExampleImage',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]