# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20150601_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='duedate',
            field=models.CharField(default='', max_length=10, null=True),
        ),
    ]
