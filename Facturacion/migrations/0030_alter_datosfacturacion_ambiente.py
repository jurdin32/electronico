# Generated by Django 3.2.8 on 2022-04-19 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0029_empresa_encabezado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosfacturacion',
            name='ambiente',
            field=models.CharField(choices=[('1', 'PRUEBAS'), ('2', 'PRODUCCIÓN')], max_length=4),
        ),
    ]