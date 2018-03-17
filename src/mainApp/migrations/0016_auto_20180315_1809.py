# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0015_auto_20180315_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='EndYear',
            field=models.PositiveIntegerField(blank=True, help_text='Use the following format: <YYYY>', validators=[django.core.validators.MaxValueValidator(2018)], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='StartYear',
            field=models.PositiveIntegerField(help_text='Use the following format: <YYYY>', validators=[django.core.validators.MaxValueValidator(2018)], default=0),
            preserve_default=False,
        ),
    ]
