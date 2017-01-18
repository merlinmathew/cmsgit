# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0006_auto_20170112_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homesliderimages1',
            old_name='image',
            new_name='bannerimage',
        ),
    ]
