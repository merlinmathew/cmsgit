# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0008_auto_20170112_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentworks',
            name='cmpny4',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='recentworks',
            name='website4',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
