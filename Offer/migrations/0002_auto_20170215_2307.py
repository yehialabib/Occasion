# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 23:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Offer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='no_of_likes',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='timestap',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='branch',
        ),
    ]
