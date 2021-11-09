# Generated by Django 3.2.8 on 2021-10-28 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocumentosElectronicos', '0004_alter_detallesfactura_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='factura',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
