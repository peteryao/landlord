# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0007_unit_venmo_access_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='venmo_access_token',
        ),
        migrations.AddField(
            model_name='tenant',
            name='venmo_access_token',
            field=models.CharField(default=b'NULL', max_length=128),
            preserve_default=True,
        ),
    ]
