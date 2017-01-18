# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0003_auto_20170111_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homemodel',
            name='company1',
            field=models.CharField(max_length=255, null=True, verbose_name='company01', blank=True),
        ),
        migrations.AlterField(
            model_name='homemodel',
            name='company2',
            field=models.CharField(max_length=255, null=True, verbose_name='company02', blank=True),
        ),
        migrations.AlterField(
            model_name='homemodel',
            name='name1',
            field=models.CharField(max_length=255, null=True, verbose_name='name01', blank=True),
        ),
        migrations.AlterField(
            model_name='homemodel',
            name='name2',
            field=models.CharField(max_length=255, null=True, verbose_name='name02', blank=True),
        ),
        migrations.AlterField(
            model_name='homemodel',
            name='testimonial1',
            field=models.CharField(max_length=255, null=True, verbose_name=b'testimonial01', blank=True),
        ),
        migrations.AlterField(
            model_name='homemodel',
            name='testimonial2',
            field=models.CharField(max_length=255, null=True, verbose_name=b'testimonial02', blank=True),
        ),
    ]
