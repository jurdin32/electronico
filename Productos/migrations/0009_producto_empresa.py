# Generated by Django 3.2.8 on 2021-10-28 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0016_auto_20211028_1055'),
        ('Productos', '0008_auto_20211019_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Facturacion.empresa'),
        ),
    ]
