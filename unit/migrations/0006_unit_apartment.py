# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mgmt', '0001_initial'),
        ('unit', '0005_remove_unit_apartment'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='apartment',
            field=models.ForeignKey(to='mgmt.Apartment'),
            preserve_default=False,
        ),
    ]
