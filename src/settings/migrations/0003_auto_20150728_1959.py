# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20150728_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdetail',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
