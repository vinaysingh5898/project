# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('Ratings', models.IntegerField(default=0)),
                ('Name', models.CharField(max_length=120)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=120, null=True, blank=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=120, null=True, blank=True)),
                ('Publication', models.CharField(max_length=120, null=True, blank=True)),
                ('Address', models.CharField(max_length=500, null=True, blank=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_no', models.IntegerField(default=0)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='Publisher',
            field=models.OneToOneField(to='mainApp.Publishers'),
        ),
    ]
