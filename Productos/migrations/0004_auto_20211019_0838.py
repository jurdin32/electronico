# Generated by Django 3.2.8 on 2021-10-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_alter_producto_impuesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='producto',
            name='valor_impuesto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
