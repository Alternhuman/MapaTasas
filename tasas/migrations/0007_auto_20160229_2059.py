# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 19:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasas', '0006_auto_20160228_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasa',
            name='url',
            field=models.URLField(help_text='URL del documento oficial', validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
