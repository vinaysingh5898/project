# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
import django.core.validators
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0003_auto_20180314_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Address', models.CharField(null=True, blank=True, max_length=500)),
                ('Phone', models.DecimalField(null=True, blank=True, decimal_places=False, max_digits=10)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('User', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Book', models.OneToOneField(to='mainApp.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BookEdition',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Edition', models.CharField(default='1', max_length=20)),
                ('YearOfPublication', models.PositiveIntegerField(help_text='Use the following format: <YYYY>', validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)])),
                ('Price', models.IntegerField(default=0)),
                ('CoverImage', models.ImageField(upload_to='img/BookCvr/', default='img/BookCvr/no-img.jpg')),
                ('PageCount', models.IntegerField(default=0)),
                ('Discount', models.PositiveIntegerField(help_text='Discount should be between 0% to 100%', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('AvailableNoOfCopies', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Book', models.OneToOneField(to='mainApp.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Name', models.CharField(null=True, blank=True, max_length=120)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('PriPhone', models.DecimalField(decimal_places=False, max_digits=10)),
                ('SecPhone', models.DecimalField(null=True, blank=True, decimal_places=False, max_digits=10)),
                ('LandMark', models.CharField(null=True, blank=True, max_length=500)),
                ('City', models.CharField(default='', max_length=500)),
                ('State', models.CharField(default='', max_length=500)),
                ('Country', models.CharField(default='', max_length=500)),
                ('PinCode', models.DecimalField(decimal_places=False, max_digits=6)),
                ('AddressLine', models.CharField(null=True, blank=True, max_length=500)),
                ('ProfileImg', models.ImageField(upload_to='img/Customer/', default='img/CustomerPic/no-img.jpg')),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Content', models.CharField(default='', max_length=500)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('CustomerReadStatus', models.NullBooleanField()),
                ('SellerReadStatus', models.NullBooleanField()),
                ('AdminReadStatus', models.NullBooleanField()),
                ('Customer_id', models.IntegerField(default=0)),
                ('Seller_id', models.IntegerField(default=0)),
                ('Admin_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('DateOfPurchase', models.DateTimeField(auto_now_add=True)),
                ('DateOfShipment', models.DateTimeField(blank=True)),
                ('DateOfDelivary', models.DateTimeField(blank=True)),
                ('Tag', models.CharField(null=True, blank=True, max_length=500)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Book', models.OneToOneField(to='mainApp.BookEdition')),
                ('Customer', models.OneToOneField(to='mainApp.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Content', models.CharField(null=True, blank=True, max_length=500)),
                ('Ratings', models.IntegerField(default=0)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Book', models.OneToOneField(to='mainApp.BookEdition')),
                ('Customer', models.OneToOneField(to='mainApp.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('PriPhone', models.DecimalField(decimal_places=False, max_digits=10)),
                ('SecPhone', models.DecimalField(null=True, blank=True, decimal_places=False, max_digits=10)),
                ('VerificationStatus', models.IntegerField(default=0)),
                ('BlockStatus', models.IntegerField(default=0)),
                ('Ratings', models.IntegerField(default=0)),
                ('LandMark', models.CharField(null=True, blank=True, max_length=500)),
                ('City', models.CharField(default='', max_length=500)),
                ('State', models.CharField(default='', max_length=500)),
                ('Country', models.CharField(default='', max_length=500)),
                ('PinCode', models.DecimalField(decimal_places=False, max_digits=6)),
                ('AddressLine', models.CharField(null=True, blank=True, max_length=500)),
                ('ProfileImg', models.ImageField(upload_to='img/SellerPic/', default='img/SellerPic/no-img.jpg')),
                ('Remark', models.CharField(null=True, blank=True, max_length=500)),
                ('AdharNo', models.DecimalField(null=True, blank=True, decimal_places=False, max_digits=12)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('AdminBlocked', models.OneToOneField(related_name='username', to='mainApp.Admin')),
                ('AdminVerified', models.OneToOneField(related_name='email', to='mainApp.Admin')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='Created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 14, 23, 45, 53, 36536, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='Updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 14, 23, 46, 26, 150961, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookedition',
            name='Seller',
            field=models.OneToOneField(to='mainApp.Seller'),
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='Category',
            field=models.OneToOneField(to='mainApp.Category'),
        ),
    ]
