# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20150628_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.AddField(
            model_name='category',
            name='category_parent',
            field=models.ForeignKey(related_name='category_children', blank=True, to='vehicles.Category', null=True),
        ),
    ]
