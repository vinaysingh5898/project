# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0016_auto_20180315_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='EndYear',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2018)], null=True, help_text='Use the following format: <YYYY>', blank=True),
        ),
    ]
