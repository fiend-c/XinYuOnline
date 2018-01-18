# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-18 19:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180118_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='apps/users/banner/%Y/%m', verbose_name='\u8f6e\u64ad\u56fe'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u53d1\u9001\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '\u6ce8\u518c'), ('forget', '\u627e\u56de\u5bc6\u7801')], max_length=10, verbose_name='\u9a8c\u8bc1\u7801\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u624b\u673a\u53f7'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='vavtar',
            field=models.ImageField(default='apps/users/image/default.png', upload_to='apps/users/image/%Y/%m', verbose_name='\u5934\u50cf'),
        ),
    ]