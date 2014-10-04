# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0006_unit_apartment'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='venmo_access_token',
            field=models.CharField(default=b'NULL', max_length=128),
            preserve_default=True,
        ),
    ]
