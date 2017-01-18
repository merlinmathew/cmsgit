# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cms_plugins_about', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('about_text', models.CharField(max_length=255, null=True, verbose_name=b'About', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='BottomLogos',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cms_plugins_bottomlogos', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('img1', models.ImageField(null=True, upload_to=b'bottomlogos')),
                ('img2', models.ImageField(null=True, upload_to=b'bottomlogos')),
                ('img3', models.ImageField(null=True, upload_to=b'bottomlogos')),
                ('img4', models.ImageField(null=True, upload_to=b'bottomlogos')),
                ('img5', models.ImageField(null=True, upload_to=b'bottomlogos')),
                ('img6', models.ImageField(null=True, upload_to=b'bottomlogos')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='HomeModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cms_plugins_homemodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('testimonial1', models.CharField(max_length=255, null=True, verbose_name=b'testimonial', blank=True)),
                ('name1', models.CharField(max_length=255, null=True, verbose_name='name', blank=True)),
                ('company1', models.CharField(max_length=255, null=True, verbose_name='company', blank=True)),
                ('testimonial2', models.CharField(max_length=255, null=True, verbose_name=b'testimonial1', blank=True)),
                ('name2', models.CharField(max_length=255, null=True, verbose_name='name1', blank=True)),
                ('company2', models.CharField(max_length=255, null=True, verbose_name='company1', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='HomeSliderImages1',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cms_plugins_homesliderimages1', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('slider1', models.ImageField(null=True, upload_to=b'sliderimages')),
                ('title1', models.CharField(max_length=255, null=True, verbose_name=b'title1', blank=True)),
                ('desc1', models.CharField(max_length=255, null=True, verbose_name=b'desc1', blank=True)),
                ('slider2', models.ImageField(upload_to=b'sliderimages', null=True, verbose_name='slider image2')),
                ('title2', models.CharField(max_length=255, null=True, verbose_name=b'title2', blank=True)),
                ('desc2', models.CharField(max_length=255, null=True, verbose_name=b'desc2', blank=True)),
                ('slider3', models.ImageField(upload_to=b'sliderimages', null=True, verbose_name='slider image3')),
                ('title3', models.CharField(max_length=255, null=True, verbose_name=b'title3', blank=True)),
                ('desc3', models.CharField(max_length=255, null=True, verbose_name=b'desc3', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Mid',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cms_plugins_mid', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('mimg', models.ImageField(null=True, upload_to=b'mm')),
                ('num1', models.CharField(max_length=255, null=True, blank=True)),
                ('wri1', models.CharField(max_length=255, null=True, blank=True)),
                ('num2', models.CharField(max_length=255, null=True, blank=True)),
                ('wri2', models.CharField(max_length=255, null=True, blank=True)),
                ('num3', models.CharField(max_length=255, null=True, blank=True)),
                ('wri3', models.CharField(max_length=255, null=True, blank=True)),
                ('num4', models.CharField(max_length=255, null=True, blank=True)),
                ('wri4', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='MidLo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cms_plugins_midlo', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('im1', models.ImageField(null=True, upload_to=b'mmm')),
                ('say1', models.CharField(max_length=255, null=True, blank=True)),
                ('im2', models.ImageField(null=True, upload_to=b'mmm')),
                ('say2', models.CharField(max_length=255, null=True, blank=True)),
                ('im3', models.ImageField(null=True, upload_to=b'mmm')),
                ('say3', models.CharField(max_length=255, null=True, blank=True)),
                ('im4', models.ImageField(null=True, upload_to=b'mmm')),
                ('say4', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='RecentWorks',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cms_plugins_recentworks', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('rw1', models.ImageField(null=True, upload_to=b'work')),
                ('website1', models.CharField(max_length=255, null=True, blank=True)),
                ('cmpny1', models.CharField(max_length=255, null=True, blank=True)),
                ('rw2', models.ImageField(null=True, upload_to=b'work')),
                ('website2', models.CharField(max_length=255, null=True, blank=True)),
                ('cmpny2', models.CharField(max_length=255, null=True, blank=True)),
                ('rw3', models.ImageField(null=True, upload_to=b'work')),
                ('website3', models.CharField(max_length=255, null=True, blank=True)),
                ('cmpny3', models.CharField(max_length=255, null=True, blank=True)),
                ('rw4', models.ImageField(null=True, upload_to=b'work')),
                ('website4', models.CharField(max_length=255, null=True, blank=True)),
                ('cmpny4', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Text1',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cms_plugins_text1', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, null=True, verbose_name=b'text1', blank=True)),
                ('boldtitle', models.CharField(max_length=255, null=True, verbose_name=b'boldtitle1', blank=True)),
                ('desc', models.CharField(max_length=255, null=True, verbose_name=b'desc1', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Text2',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='cms_plugins_text2', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, null=True, verbose_name=b'text2', blank=True)),
                ('boldtitle', models.CharField(max_length=255, null=True, verbose_name=b'boldtitle2', blank=True)),
                ('desc', models.CharField(max_length=255, null=True, verbose_name=b'desc2', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
