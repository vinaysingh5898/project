# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0017_auto_20180315_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='EndYear',
            field=models.PositiveIntegerField(help_text='Use the following format: <YYYY>', null=True, blank=True, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(2018)]),
        ),
        migrations.AlterField(
            model_name='author',
            name='StartYear',
            field=models.PositiveIntegerField(help_text='Use the following format: <YYYY>', validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(2018)]),
        ),
    ]
