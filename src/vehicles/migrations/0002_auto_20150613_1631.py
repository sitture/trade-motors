# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('category_image', models.ImageField(upload_to=b'category_images', verbose_name=b'Image')),
            ],
        ),
        migrations.DeleteModel(
            name='VehicleCategory',
        ),
    ]
