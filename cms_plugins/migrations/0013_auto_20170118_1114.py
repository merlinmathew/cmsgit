# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('cms_plugins', '0012_auto_20170118_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cms_plugins_testimonial', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('testimonial', models.CharField(max_length=255, null=True, verbose_name=b'testimonial', blank=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name=b'name', blank=True)),
                ('company', models.CharField(max_length=255, null=True, verbose_name=b'company', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='homem',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='HomeM',
        ),
    ]
