# Generated by Django 3.2.8 on 2021-11-06 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0022_datosfacturacion_ambiente'),
        ('Personas', '0002_clientes_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Facturacion.empresa'),
        ),
    ]
