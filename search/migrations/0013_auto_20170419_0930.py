# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0012_auto_20170419_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatars',
            name='DateCreated',
            field=models.DateTimeField(blank=True, db_column='Datecreated', default=django.utils.timezone.now, null=True),
        ),
    ]