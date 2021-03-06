# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-02 15:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_code', models.CharField(db_index=True, default=b'', max_length=128)),
                ('code', models.CharField(default=b'', max_length=128)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('area', models.CharField(default=b'', max_length=128)),
                ('industry', models.CharField(default=b'', max_length=128)),
                ('market', models.CharField(default=b'', max_length=128)),
                ('exchange', models.CharField(default=b'', max_length=128)),
                ('status', models.CharField(default=b'', max_length=128)),
                ('close_date', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('is_hs', models.CharField(default=b'', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='StockDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_date', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('pre_close', models.FloatField(blank=True, default=0.0, null=True)),
                ('open', models.FloatField(blank=True, default=0.0, null=True)),
                ('close', models.FloatField(blank=True, default=0.0, null=True)),
                ('high', models.FloatField(blank=True, default=0.0, null=True)),
                ('low', models.FloatField(blank=True, default=0.0, null=True)),
                ('change', models.FloatField(blank=True, default=0.0, null=True)),
                ('change_percentile', models.FloatField(blank=True, default=0.0, null=True)),
                ('volume', models.FloatField(blank=True, default=0.0, null=True)),
                ('amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_days', to='data.Stock')),
            ],
        ),
    ]
