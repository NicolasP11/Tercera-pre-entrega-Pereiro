# Generated by Django 4.2.5 on 2023-10-06 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppRest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comida',
            name='descripcion',
        ),
    ]
