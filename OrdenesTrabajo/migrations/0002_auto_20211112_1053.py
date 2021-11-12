# Generated by Django 3.2.8 on 2021-11-12 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0025_datosfacturacion_secual_orden_trabajo'),
        ('OrdenesTrabajo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='abono',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='orden',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Facturacion.empresa'),
        ),
        migrations.AddField(
            model_name='orden',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='orden',
            name='total_cobrar',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
