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
            name='price',
            field=models.DecimalField(null=True, verbose_name=b'Price (Optional)', max_digits=10, decimal_places=2, blank=True),
        ),
    ]
