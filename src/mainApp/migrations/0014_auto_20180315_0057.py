# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_auto_20180315_0054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='user',
            new_name='User',
        ),
    ]
