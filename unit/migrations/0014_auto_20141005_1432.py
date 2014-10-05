# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0013_auto_20141005_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2014, 10, 12, 14, 32, 12, 609786)),
        ),
    ]
