# Generated by Django 4.2 on 2023-10-03 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_habitacion_reserva'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habitacion',
            old_name='tipo_habitacion',
            new_name='tipo',
        ),
    ]
