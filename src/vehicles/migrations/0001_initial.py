# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=50, verbose_name=b'Category Name')),
                ('category_image', models.ImageField(upload_to=b'category_images', verbose_name=b'Category Image')),
                ('show_on_home', models.BooleanField(verbose_name=b'Show on Homepage?')),
            ],
        ),
    ]
