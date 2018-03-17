# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0020_auto_20180316_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='Address',
            field=models.TextField(max_length=500, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='Content',
            field=models.TextField(max_length=500, default=''),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='Address',
            field=models.TextField(max_length=500, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='Content',
            field=models.TextField(max_length=500, blank=True, null=True),
        ),
    ]
