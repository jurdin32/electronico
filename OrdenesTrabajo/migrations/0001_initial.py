# Generated by Django 3.2.8 on 2021-11-12 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Personas', '0003_clientes_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('secuencial', models.CharField(default='000000000', max_length=9)),
                ('dispositivo_recibido', models.TextField()),
                ('marca_modelo', models.TextField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('numero_serie', models.CharField(blank=True, max_length=50, null=True)),
                ('cables_accesorios', models.TextField(blank=True, null=True)),
                ('problema_reportado', models.TextField(blank=True, null=True)),
                ('tareas_a_realizar', models.TextField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('hora_fecha_salida', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(default='EN REVISIÓN', max_length=60)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personas.clientes')),
            ],
        ),
    ]
