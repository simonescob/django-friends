# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-19 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0005_remove_friend_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
