# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
