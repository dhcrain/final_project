# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0009_auto_20160731_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='rating_fm',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='rating_user',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='rating_vendor',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_fm_like',
            field=models.ManyToManyField(null=True, related_name='fm_liked_by', to='review_app.FarmersMarket'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_vendor_like',
            field=models.ManyToManyField(null=True, related_name='vendor_liked_by', to='review_app.FarmersMarket'),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
