# Generated by Django 3.2.8 on 2022-02-25 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0026_alter_datosfacturacion_secual_orden_trabajo'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosfacturacion',
            name='secuencial_proforma',
            field=models.IntegerField(default=0),
        ),
    ]
