# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('cms_plugins', '0004_auto_20170111_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeM',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cms_plugins_homem', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('testimonial1', models.CharField(max_length=255, null=True, verbose_name=b'testimonial01', blank=True)),
                ('name1', models.CharField(max_length=255, null=True, verbose_name=b'name01', blank=True)),
                ('company1', models.CharField(max_length=255, null=True, verbose_name=b'company01', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='homemodel',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='HomeModel',
        ),
    ]
