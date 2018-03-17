# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20180314_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='Phone_no',
        ),
        migrations.AddField(
            model_name='publisher',
            name='Phone',
            field=models.DecimalField(null=True, decimal_places=False, blank=True, max_digits=10),
        ),
    ]
