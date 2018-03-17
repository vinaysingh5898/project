# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_auto_20180315_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcategory',
            name='Book',
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='Book',
            field=models.ManyToManyField(blank=True, to='mainApp.Book', null=True),
        ),
        migrations.RemoveField(
            model_name='bookcategory',
            name='Category',
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='Category',
            field=models.ManyToManyField(to='mainApp.Category', related_name='Category_id'),
        ),
    ]
