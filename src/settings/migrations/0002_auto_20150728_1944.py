# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactdetail',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='county',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 19, 44, 19, 77488), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 19, 44, 33, 549425), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='country',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='full_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='postcode',
            field=models.CharField(max_length=20),
        ),
    ]
