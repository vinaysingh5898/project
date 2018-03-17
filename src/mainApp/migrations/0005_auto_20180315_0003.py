# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20180314_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='Email',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='bookcategory',
            name='Category',
            field=models.OneToOneField(related_name='Category_id', to='mainApp.Category'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='AdminBlocked',
            field=models.OneToOneField(related_name='AdminBlocked_id', to='mainApp.Admin'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='AdminVerified',
            field=models.OneToOneField(related_name='AdminVerified_id', to='mainApp.Admin'),
        ),
    ]
