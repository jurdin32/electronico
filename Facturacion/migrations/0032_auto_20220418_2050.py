# Generated by Django 3.2.8 on 2022-04-19 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0031_alter_webservices_tipo_ambiente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosfacturacion',
            name='ambiente',
            field=models.IntegerField(choices=[(1, 'PRUEBAS'), (2, 'PRODUCCIÓN')]),
        ),
        migrations.AlterField(
            model_name='webservices',
            name='tipo_ambiente',
            field=models.IntegerField(choices=[(1, 'PRUEBAS'), (2, 'PRODUCCIÓN')], default=1, max_length=1),
        ),
    ]