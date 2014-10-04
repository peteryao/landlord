# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0002_unit_apartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='apartment',
            field=models.ForeignKey(default=1, to='mgmt.Apartment'),
        ),
    ]
