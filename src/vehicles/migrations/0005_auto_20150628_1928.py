# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_auto_20150628_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorytype',
            name='category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('category_name',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='v_category_type',
        ),
        migrations.AddField(
            model_name='category',
            name='category_display_order',
            field=models.IntegerField(default=0, verbose_name=b'Display Order'),
        ),
        migrations.DeleteModel(
            name='CategoryType',
        ),
    ]
