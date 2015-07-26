# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_auto_20150726_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='show_on_home_page',
            field=models.BooleanField(default=False, verbose_name=b'Show on Homepage?'),
        ),
    ]
