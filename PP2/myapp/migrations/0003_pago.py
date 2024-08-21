# Generated by Django 5.0.3 on 2024-08-12 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_persona_fecha_pago_persona_monto_pagado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.persona')),
            ],
        ),
    ]
