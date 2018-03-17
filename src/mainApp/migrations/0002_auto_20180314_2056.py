# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=120, null=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('Author', models.OneToOneField(to='mainApp.Author')),
                ('Book', models.OneToOneField(to='mainApp.Book')),
            ],
        ),
        migrations.RenameModel(
            old_name='Publishers',
            new_name='Publisher',
        ),
        migrations.RemoveField(
            model_name='books',
            name='Publisher',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.AddField(
            model_name='book',
            name='Publisher',
            field=models.OneToOneField(to='mainApp.Publisher'),
        ),
    ]
