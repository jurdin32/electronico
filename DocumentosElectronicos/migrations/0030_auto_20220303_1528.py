# Generated by Django 3.2.8 on 2022-03-03 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocumentosElectronicos', '0029_factura_formapago'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecuentascobrar',
            name='detalle',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='detallecuentascobrar',
            name='tipo',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]