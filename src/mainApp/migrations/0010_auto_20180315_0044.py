# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_auto_20180315_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcategory',
            name='Book',
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='Book',
            field=models.ForeignKey(blank=True, to='mainApp.Book', default=0),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='bookcategory',
            name='Category',
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='Category',
            field=models.ForeignKey(related_name='Category_id', to='mainApp.Category', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seller',
            name='AdminBlocked',
            field=models.ForeignKey(related_name='AdminBlocked_id', blank=True, to='mainApp.Admin'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='AdminVerified',
            field=models.ForeignKey(related_name='AdminVerified_id', blank=True, to='mainApp.Admin'),
        ),
    ]
