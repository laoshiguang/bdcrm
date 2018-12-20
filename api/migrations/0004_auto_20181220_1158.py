# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-20 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181219_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_id', models.CharField(max_length=16)),
                ('dev_id', models.CharField(max_length=16)),
                ('token', models.CharField(max_length=32)),
                ('data', models.CharField(max_length=512)),
                ('recode', models.IntegerField(choices=[(0, '成功'), (1001, 'token不能为空'), (1002, '设备ID不能为空'), (1003, '消息ID不能为空'), (1004, '消息ID错误'), (1005, 'token验证失败'), (1007, '设备已离线'), (1006, '设备ID验证失败'), (3000, 'socket服务器错误')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('uid', models.CharField(max_length=64, unique=True, verbose_name='个人唯一ID')),
                ('wx_id', models.CharField(blank=True, db_index=True, max_length=128, null=True, verbose_name='微信ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=32)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='type',
            field=models.IntegerField(default=1, verbose_name='设备种类'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='ICCID',
            field=models.CharField(max_length=32, unique=True, verbose_name='设备ICCID'),
        ),
        migrations.AlterField(
            model_name='device',
            name='IC_Card',
            field=models.CharField(max_length=16, verbose_name='物联网卡号'),
        ),
        migrations.AlterField(
            model_name='device',
            name='dev_id',
            field=models.CharField(max_length=16, unique=True, verbose_name='设备ID'),
        ),
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='设备状态'),
        ),
    ]
