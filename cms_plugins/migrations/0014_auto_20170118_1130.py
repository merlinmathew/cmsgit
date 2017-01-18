# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0013_auto_20170118_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homesliderimages1',
            old_name='slider1',
            new_name='bannerimage',
        ),
        migrations.RenameField(
            model_name='homesliderimages1',
            old_name='desc1',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='homesliderimages1',
            old_name='title1',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='homesliderimages1',
            name='desc2',
        ),
        migrations.RemoveField(
            model_name='homesliderimages1',
            name='desc3',
        ),
        migrations.RemoveField(
            model_name='homesliderimages1',
            name='slider2',
        ),
        migrations.RemoveField(
            model_name='homesliderimages1',
            name='slider3',
        ),
        migrations.RemoveField(
            model_name='homesliderimages1',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='homesliderimages1',
            name='title3',
        ),
    ]
