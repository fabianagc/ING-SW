# Generated by Django 4.2 on 2023-10-02 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('num_habitacion', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('tipo_habitacion', models.CharField(max_length=20)),
                ('precio', models.CharField(max_length=20)),
                ('estado_ocupacion', models.CharField(max_length=20)),
                ('capacidad', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('num_reserva', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('fecha_entrada', models.CharField(max_length=20)),
                ('fecha_salida', models.CharField(max_length=20)),
                ('estado_reserva', models.CharField(max_length=20)),
                ('nro_personas', models.CharField(max_length=20)),
                ('estado_pago', models.CharField(max_length=20)),
                ('medio_pago', models.CharField(max_length=20)),
                ('comentario', models.CharField(max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.clientes')),
            ],
        ),
    ]
