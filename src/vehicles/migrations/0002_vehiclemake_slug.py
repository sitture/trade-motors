# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclemake',
            name='slug',
            field=models.SlugField(default='toyota', unique=True),
            preserve_default=False,
        ),
    ]
