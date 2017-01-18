# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0010_auto_20170118_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='midlo',
            name='im2',
        ),
        migrations.RemoveField(
            model_name='midlo',
            name='im3',
        ),
        migrations.RemoveField(
            model_name='midlo',
            name='im4',
        ),
        migrations.RemoveField(
            model_name='midlo',
            name='say2',
        ),
        migrations.RemoveField(
            model_name='midlo',
            name='say3',
        ),
        migrations.RemoveField(
            model_name='midlo',
            name='say4',
        ),
    ]
