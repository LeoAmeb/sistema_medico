# Generated by Django 3.2.6 on 2021-11-27 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienes', '0005_bienes_codigo_barras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bienes',
            name='codigo_barras',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
