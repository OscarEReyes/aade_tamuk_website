# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-20 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_newspost_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('title', models.CharField(max_length=64)),
                ('body', models.CharField(max_length=256)),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
