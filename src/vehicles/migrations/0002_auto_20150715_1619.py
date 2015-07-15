# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='colour',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Colour', blank=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Fuel Type', choices=[(b'petrol', b'Petrol'), (b'diesel', b'Diesel')]),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='mileage',
            field=models.IntegerField(max_length=10, null=True, verbose_name=b'Mileage', blank=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='transmission',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Transmission', choices=[(b'automatic', b'Automatic'), (b'manual', b'Manual')]),
        ),
    ]
