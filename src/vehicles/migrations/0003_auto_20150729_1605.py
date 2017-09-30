# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_vehicle_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='price',
            field=models.IntegerField(null=True, verbose_name=b'Price (Optional)', blank=True),
        ),
    ]
