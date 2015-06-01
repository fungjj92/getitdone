# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20150601_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='duedate',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]
