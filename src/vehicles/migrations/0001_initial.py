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
                ('category_image', models.ImageField(upload_to=b'category_images', verbose_name=b'Image', blank=True)),
                ('category_display_order', models.IntegerField(default=999, verbose_name=b'Display Order')),
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
                ('desc', ckeditor.fields.RichTextField(verbose_name=b'Description')),
                ('slug', models.SlugField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='vehicles.Category')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'vehicle_images', verbose_name=b'Image')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('vehicle', models.ForeignKey(to='vehicles.Vehicle')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='VehicleMake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('v_make', models.CharField(max_length=50, verbose_name=b'Make')),
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
