# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_auto_20150715_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='mileage',
            field=models.IntegerField(null=True, verbose_name=b'Mileage', blank=True),
        ),
    ]
