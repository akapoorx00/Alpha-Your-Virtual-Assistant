# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlphaReminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder', models.CharField(max_length=500)),
            ],
        ),
    ]
