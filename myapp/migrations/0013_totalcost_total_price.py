# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-13 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20190713_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalcost',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
    ]
