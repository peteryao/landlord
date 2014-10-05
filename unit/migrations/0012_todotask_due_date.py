# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0011_unit_moxtra_binder_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotask',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2014, 10, 12, 14, 21, 54, 591530)),
            preserve_default=True,
        ),
    ]
