# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-19 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0007_auto_20161118_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
