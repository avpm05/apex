# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20170419_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatars',
            name='DateCreated',
            field=models.DateField(auto_created=True, blank=True, db_column='Datecreated', null=True),
        ),
    ]
