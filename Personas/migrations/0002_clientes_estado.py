# Generated by Django 3.2.8 on 2021-11-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
