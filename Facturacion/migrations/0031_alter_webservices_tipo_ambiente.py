# Generated by Django 3.2.8 on 2022-04-19 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0030_alter_datosfacturacion_ambiente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webservices',
            name='tipo_ambiente',
            field=models.CharField(choices=[('1', 'PRUEBAS'), ('2', 'PRODUCCIÓN')], default=1, max_length=1),
        ),
    ]