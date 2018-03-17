# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_auto_20180315_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Name',
            field=models.CharField(max_length=120, default=''),
        ),
    ]
