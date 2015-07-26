# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleimage',
            name='vehicle',
            field=models.ForeignKey(related_name='images', to='vehicles.Vehicle'),
        ),
    ]
