# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('created_on', models.DateTimeField(verbose_name=b'date added to portfolio')),
                ('last_updated', models.DateTimeField(verbose_name=b'last updated')),
                ('logo_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Rounds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=50)),
                ('cash_in', models.IntegerField(default=0)),
            ],
        ),
    ]
