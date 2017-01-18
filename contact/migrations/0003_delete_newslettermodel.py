# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_newslettermodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsletterModel',
        ),
    ]
