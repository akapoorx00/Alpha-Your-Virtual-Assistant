# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlphaKnowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('response', models.CharField(max_length=500)),
            ],
        ),
    ]
