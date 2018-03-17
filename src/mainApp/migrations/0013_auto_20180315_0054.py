# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0012_auto_20180315_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='AdminBlocked',
            field=models.ForeignKey(to='mainApp.Admin', related_name='AdminBlocked_id', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='AdminVerified',
            field=models.ForeignKey(to='mainApp.Admin', related_name='AdminVerified_id', null=True, blank=True),
        ),
    ]
