# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=38)),
                ('show', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iso', models.CharField(max_length=2, verbose_name=b'ISO Code')),
                ('name', models.CharField(max_length=30, verbose_name=b'Country name')),
                ('show', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='country.Country'),
        ),
    ]
