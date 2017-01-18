# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0011_auto_20170118_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recentworks',
            name='cmpny2',
        ),
        migrations.RemoveField(
            model_name='recentworks',
            name='cmpny3',
        ),
        migrations.RemoveField(
            model_name='recentworks',
            name='cmpny4',
        ),
        migrations.RemoveField(
            model_name='recentworks',
            name='rw2',
        ),
        migrations.RemoveField(
            model_name='recentworks',
            name='rw3',
        ),
        migrations.RemoveField(
            model_name='recentworks',
            name='rw4',
        ),
        migrations.RemoveField(
            model_name='recentworks',
            name='website2',
        ),
        migrations.RemoveField(
            model_name='recentworks',
            name='website3',
        ),
        migrations.RemoveField(
            model_name='recentworks',
            name='website4',
        ),
    ]
