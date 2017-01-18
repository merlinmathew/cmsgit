# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('cms_plugins', '0015_auto_20170118_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='MidBannerImage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cms_plugins_midbannerimage', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('image', models.ImageField(null=True, upload_to=b'images')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='mid',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='mid',
            name='description3',
        ),
        migrations.RemoveField(
            model_name='mid',
            name='description4',
        ),
        migrations.RemoveField(
            model_name='mid',
            name='image',
        ),
        migrations.RemoveField(
            model_name='mid',
            name='number2',
        ),
        migrations.RemoveField(
            model_name='mid',
            name='number3',
        ),
        migrations.RemoveField(
            model_name='mid',
            name='number4',
        ),
    ]
