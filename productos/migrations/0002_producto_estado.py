# Generated by Django 4.2.7 on 2023-11-12 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[('1', 'En Stock'), ('2', 'Agotado')], default=1, max_length=2),
        ),
    ]