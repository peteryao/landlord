# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0008_auto_20141004_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='venmo_photo',
            field=models.URLField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
