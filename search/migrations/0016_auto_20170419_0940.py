# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0015_auto_20170419_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatars',
            name='DateCreated',
            field=models.DateTimeField(db_column='Datecreated', default=django.utils.timezone.now),
        ),
    ]
