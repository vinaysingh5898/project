# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0019_kart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedition',
            name='YearOfPublication',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(2018)], help_text='Use the following format: <YYYY>'),
        ),
    ]
