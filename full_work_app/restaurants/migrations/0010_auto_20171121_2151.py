# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 16:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import restaurants.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0009_auto_20171121_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[restaurants.validators.validate_category]),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
