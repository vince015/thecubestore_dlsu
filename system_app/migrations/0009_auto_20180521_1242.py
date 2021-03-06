# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-21 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_app', '0008_auto_20170808_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name': 'Sale'},
        ),
        migrations.AlterField(
            model_name='item',
            name='commission',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='payout',
            name='remarks',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
