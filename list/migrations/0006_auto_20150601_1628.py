# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_auto_20150601_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='duedate',
            field=models.CharField(default='', null=True, blank=True, max_length=10),
        ),
    ]
