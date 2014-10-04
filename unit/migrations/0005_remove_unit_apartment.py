# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0004_auto_20141004_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='apartment',
        ),
    ]
