# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_contactdetail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactDetail',
        ),
    ]
