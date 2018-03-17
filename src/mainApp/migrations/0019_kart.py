# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0018_auto_20180315_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kart',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Book', models.ForeignKey(to='mainApp.BookEdition')),
                ('Customer', models.ForeignKey(to='mainApp.Customer')),
            ],
        ),
    ]
