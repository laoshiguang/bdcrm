# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-20 06:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181220_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceToGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='商品名称')),
                ('old_price', models.FloatField(verbose_name='商品原价')),
                ('new_price', models.FloatField(verbose_name='商品现价')),
                ('desc', models.CharField(max_length=256, verbose_name='商品描述')),
            ],
        ),
        migrations.AddField(
            model_name='devicetogoods',
            name='goods_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Goods'),
        ),
    ]
