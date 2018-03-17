# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0011_auto_20180315_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Publisher',
            field=models.ForeignKey(to='mainApp.Publisher'),
        ),
        migrations.AlterField(
            model_name='bookauthor',
            name='Author',
            field=models.ForeignKey(to='mainApp.Author'),
        ),
        migrations.AlterField(
            model_name='bookauthor',
            name='Book',
            field=models.ForeignKey(to='mainApp.Book'),
        ),
        migrations.AlterField(
            model_name='bookedition',
            name='Book',
            field=models.ForeignKey(to='mainApp.Book'),
        ),
        migrations.AlterField(
            model_name='bookedition',
            name='Seller',
            field=models.ForeignKey(to='mainApp.Seller'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Book',
            field=models.ForeignKey(to='mainApp.BookEdition'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Customer',
            field=models.ForeignKey(to='mainApp.Customer'),
        ),
        migrations.AlterField(
            model_name='review',
            name='Book',
            field=models.ForeignKey(to='mainApp.BookEdition'),
        ),
        migrations.AlterField(
            model_name='review',
            name='Customer',
            field=models.ForeignKey(to='mainApp.Customer'),
        ),
    ]
