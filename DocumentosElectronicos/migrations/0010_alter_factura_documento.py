# Generated by Django 3.2.8 on 2021-10-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocumentosElectronicos', '0009_factura_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='documento',
            field=models.TextField(blank=True, null=True),
        ),
    ]
