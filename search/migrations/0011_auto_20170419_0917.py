# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_auto_20170419_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatars',
            name='DateCreated',
            field=models.DateField(auto_now_add=True, db_column='Datecreated', null=True),
        ),
        migrations.AlterField(
            model_name='avatars',
            name='DateParsed',
            field=models.DateTimeField(blank=True, db_column='Dateparsed', null=True),
        ),
    ]