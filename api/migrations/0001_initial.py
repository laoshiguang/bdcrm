# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-19 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_id', models.CharField(max_length=16)),
                ('status', models.IntegerField(choices=[(1, '在线'), (2, '离线')])),
                ('ICCID', models.CharField(max_length=32)),
                ('IC_Card', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_id', models.CharField(max_length=16)),
                ('dev_id', models.CharField(max_length=16)),
                ('cmd', models.CharField(choices=[('online', '设备上线'), ('offline', '设备离线'), ('test', '数据订阅接口验证'), ('41', 'RTU上报数据'), ('42', '平台下发数据返回结果')], max_length=16)),
                ('data', models.CharField(max_length=512)),
            ],
        ),
    ]
