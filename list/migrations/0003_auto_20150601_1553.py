# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_auto_20150601_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='duedate',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
