# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadcsv', '0005_auto_20160827_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='namelist',
            name='namefile',
            field=models.FileField(upload_to='uploadcsv/static/'),
        ),
    ]