# Generated by Django 3.2.8 on 2022-02-26 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocumentosElectronicos', '0025_auto_20220225_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecuentascobrar',
            name='por_pagar',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
