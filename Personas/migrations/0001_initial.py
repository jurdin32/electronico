# Generated by Django 3.2.8 on 2021-10-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(choices=[('04', 'RUC'), ('05', 'CEDULA'), ('06', 'PASAPORTE'), ('07', 'VENTA A CONSUMIDOR FINAL'), ('08', 'IDENTIFICACIÓN DEL EXTERIOR')], max_length=2)),
                ('nombres_apellidos', models.CharField(max_length=300)),
                ('identificacion', models.CharField(max_length=13)),
                ('direccion', models.CharField(max_length=300)),
                ('telefono', models.CharField(max_length=13)),
                ('correo_electronico', models.EmailField(max_length=300)),
            ],
        ),
    ]
