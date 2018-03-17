# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_auto_20180315_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcategory',
            name='Book',
            field=models.ForeignKey(to='mainApp.Book', default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='bookcategory',
            name='Category',
            field=models.ForeignKey(to='mainApp.Category', related_name='Category_id', default=0),
        ),
    ]
