# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-01-16 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0007_auto_20200111_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='end',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='start',
            field=models.DateTimeField(editable=False),
        ),
    ]