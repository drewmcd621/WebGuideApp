# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0004_auto_20160428_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('date_requested', models.DateField()),
                ('sunday_open', models.TimeField()),
                ('sunday_close', models.TimeField()),
                ('monday_open', models.TimeField()),
                ('monday_close', models.TimeField()),
                ('tuesday_open', models.TimeField()),
                ('tuesday_close', models.TimeField()),
                ('wednesday_open', models.TimeField()),
                ('wednesday_close', models.TimeField()),
                ('thursday_open', models.TimeField()),
                ('thursday_close', models.TimeField()),
                ('friday_open', models.TimeField()),
                ('friday_close', models.TimeField()),
                ('saturday_open', models.TimeField()),
                ('saturday_close', models.TimeField()),
            ],
        ),
    ]
