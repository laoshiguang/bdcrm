# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-19 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181219_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receive',
            old_name='devid',
            new_name='dev_id',
        ),
        migrations.RenameField(
            model_name='receive',
            old_name='msgid',
            new_name='msg_id',
        ),
        migrations.AlterField(
            model_name='receive',
            name='data',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
