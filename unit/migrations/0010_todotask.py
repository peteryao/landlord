# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0009_tenant_venmo_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('is_complete', models.BooleanField(default=False)),
                ('unit', models.ForeignKey(to='unit.Unit')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
