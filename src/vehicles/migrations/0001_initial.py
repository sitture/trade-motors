# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('category_image', models.ImageField(upload_to=b'categories', verbose_name=b'Image', blank=True)),
                ('category_display_order', models.IntegerField(default=999, verbose_name=b'Display Order')),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category_parent', models.ForeignKey(related_name='category_children', blank=True, to='vehicles.Category', null=True)),
            ],
            options={
                'ordering': ['category_display_order', 'category_name'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model', models.CharField(max_length=100, verbose_name=b'Model')),
                ('year', models.IntegerField(null=True, verbose_name=b'Year (E.g. 1990)', blank=True)),
                ('fuel_type', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Fuel Type', choices=[(b'petrol', b'Petrol'), (b'diesel', b'Diesel')])),
                ('transmission', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Transmission', choices=[(b'automatic', b'Automatic'), (b'manual', b'Manual')])),
                ('colour', models.CharField(max_length=50, null=True, verbose_name=b'Colour', blank=True)),
                ('mileage', models.IntegerField(null=True, verbose_name=b'Mileage', blank=True)),
                ('desc', ckeditor.fields.RichTextField(verbose_name=b'Description')),
                ('slug', models.SlugField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='vehicles.Category')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='VehicleImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'vehicles', verbose_name=b'Image')),
                ('main_image', models.BooleanField(default=False, verbose_name=b'Main Image?')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('vehicle', models.ForeignKey(to='vehicles.Vehicle')),
            ],
            options={
                'ordering': ['vehicle', '-timestamp'],
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='VehicleMake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('v_make', models.CharField(max_length=50, verbose_name=b'Make')),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Make',
                'verbose_name_plural': 'Makes',
            },
        ),
        migrations.AddField(
            model_name='vehicle',
            name='make',
            field=models.ForeignKey(to='vehicles.VehicleMake'),
        ),
    ]
