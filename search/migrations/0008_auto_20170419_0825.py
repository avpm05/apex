# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_avatars_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatars',
            name='ParsingUrl_FK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='search.ParsingPlan'),
        ),
    ]
