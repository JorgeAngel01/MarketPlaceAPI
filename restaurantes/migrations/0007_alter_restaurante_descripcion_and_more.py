# Generated by Django 4.2.7 on 2023-11-25 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0006_restaurante_banner_restaurante_icono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
