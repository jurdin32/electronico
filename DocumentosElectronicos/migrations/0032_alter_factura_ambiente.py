# Generated by Django 3.2.8 on 2022-03-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocumentosElectronicos', '0031_factura_ambiente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='ambiente',
            field=models.CharField(default='PRUEBAS', max_length=40),
        ),
    ]
