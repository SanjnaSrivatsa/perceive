# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 00:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0007_auto_20170219_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click_log',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
