# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0009_auto_20170118_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottomlogos',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='bottomlogos',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='bottomlogos',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='bottomlogos',
            name='img5',
        ),
        migrations.RemoveField(
            model_name='bottomlogos',
            name='img6',
        ),
        migrations.AlterField(
            model_name='recentworks',
            name='cmpny4',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recentworks',
            name='website4',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
