# Generated by Django 3.2.8 on 2021-11-01 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0021_alter_datosfacturacion_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosfacturacion',
            name='ambiente',
            field=models.IntegerField(default=1),
        ),
    ]
