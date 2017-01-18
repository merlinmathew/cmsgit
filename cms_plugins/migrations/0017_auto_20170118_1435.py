# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('cms_plugins', '0016_auto_20170118_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='midbannerimage',
            name='cmsplugin_ptr',
        ),
        migrations.AddField(
            model_name='mid',
            name='description2',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mid',
            name='description3',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mid',
            name='description4',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mid',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images'),
        ),
        migrations.AddField(
            model_name='mid',
            name='number2',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mid',
            name='number3',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mid',
            name='number4',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='MidBannerImage',
        ),
    ]
