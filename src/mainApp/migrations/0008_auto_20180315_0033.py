# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_auto_20180315_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcategory',
            name='Book',
            field=models.ManyToManyField(to='mainApp.Book', blank=True),
        ),
    ]
