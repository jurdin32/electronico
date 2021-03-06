# Generated by Django 3.2.8 on 2021-10-18 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0004_empresa_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('codigo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DatosFacturacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secuencial', models.IntegerField(default=0)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Facturacion.empresa')),
            ],
        ),
    ]
