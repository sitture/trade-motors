# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0006_auto_20150704_1838'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicleimage',
            options={'ordering': ['vehicle', '-timestamp'], 'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
    ]
