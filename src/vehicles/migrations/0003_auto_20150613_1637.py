# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_auto_20150613_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 16, 37, 40, 362678, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 16, 37, 54, 162228, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
