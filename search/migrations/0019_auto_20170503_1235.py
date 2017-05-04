# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0018_auto_20170419_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='Description',
            field=models.TextField(db_column='Description', default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sources',
            name='Type',
            field=models.CharField(blank=True, db_column='Type', max_length=30, null=True),
        ),
    ]
