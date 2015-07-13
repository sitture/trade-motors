# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=150, null=True, verbose_name=b'FullName (Optional)', blank=True)),
                ('address', models.CharField(max_length=500, verbose_name=b'Address', blank=True)),
                ('postcode', models.CharField(max_length=150, verbose_name=b'Postcode', blank=True)),
                ('city', models.CharField(max_length=150, verbose_name=b'City', blank=True)),
                ('country', models.CharField(max_length=150, verbose_name=b'Country', blank=True)),
                ('phone', models.CharField(max_length=150, blank=True)),
                ('email', models.CharField(max_length=300, verbose_name=b'Email')),
            ],
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service', models.CharField(max_length=50, verbose_name=b'Service', choices=[(b'facebook', b'Facebook'), (b'google-plus', b'Google+'), (b'twitter', b'Twitter'), (b'linkedin', b'LinkedIn'), (b'instagram', b'Instagram')])),
                ('url', models.URLField(verbose_name=b'Page Link')),
            ],
        ),
    ]
