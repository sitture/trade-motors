# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20150704_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleimage',
            name='main_image',
            field=models.BooleanField(default=False, verbose_name=b'Main Image?'),
        ),
    ]
