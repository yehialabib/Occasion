# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0002_auto_20170207_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('photo', models.CharField(max_length=200, null=True)),
                ('branch', models.CharField(max_length=1000, null=True)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('timestap', models.DateTimeField(auto_now_add=True)),
                ('no_of_likes', models.IntegerField()),
                ('views', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.client')),
            ],
        ),
    ]
