# Generated by Django 3.2.8 on 2022-02-26 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DocumentosElectronicos', '0023_factura_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuentaCobrar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('detalle', models.TextField()),
                ('estado', models.CharField(default='DEBE', max_length=20)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DocumentosElectronicos.factura')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCuentasCobrar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('abono', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DocumentosElectronicos.cuentacobrar')),
            ],
        ),
    ]
