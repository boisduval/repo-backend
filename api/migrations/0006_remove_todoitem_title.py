# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-20 16:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191018_0517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='title',
        ),
    ]
