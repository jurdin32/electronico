# Generated by Django 3.2.8 on 2021-10-18 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0006_alter_impuestos_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='PorcentajesImpuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('codigo', models.IntegerField(default=0)),
                ('impuesto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Facturacion.impuestos')),
            ],
            options={
                'verbose_name_plural': '1.2 Porcentajes de Impuestos',
            },
        ),
    ]
