# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-05 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
