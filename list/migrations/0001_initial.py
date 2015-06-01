# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('task', models.CharField(max_length=300)),
                ('duedate', models.DateField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
