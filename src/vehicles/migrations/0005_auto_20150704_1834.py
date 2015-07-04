# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_vehicleimage_main_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicleimage',
            options={'ordering': ['-timestamp', 'main_image'], 'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
    ]
