# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_app', '0003_auto_20170729_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='website',
            field=models.URLField(blank=True, max_length=128, null=True),
        ),
    ]
