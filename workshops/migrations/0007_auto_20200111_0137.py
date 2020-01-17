# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-01-11 06:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0006_auto_20200111_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='workshop_one',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workshop_one_set', to='workshops.Workshop'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='workshop_two',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workshop_two_set', to='workshops.Workshop'),
        ),
    ]