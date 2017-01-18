# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0014_auto_20170118_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bottomlogos',
            old_name='img1',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='mid',
            old_name='num1',
            new_name='description1',
        ),
        migrations.RenameField(
            model_name='mid',
            old_name='num2',
            new_name='description2',
        ),
        migrations.RenameField(
            model_name='mid',
            old_name='num3',
            new_name='description3',
        ),
        migrations.RenameField(
            model_name='mid',
            old_name='num4',
            new_name='description4',
        ),
        migrations.RenameField(
            model_name='mid',
            old_name='wri1',
            new_name='number1',
        ),
        migrations.RenameField(
            model_name='mid',
            old_name='wri2',
            new_name='number2',
        ),
        migrations.RenameField(
            model_name='mid',
            old_name='wri3',
            new_name='number3',
        ),
        migrations.RenameField(
            model_name='mid',
            old_name='wri4',
            new_name='number4',
        ),
        migrations.RenameField(
            model_name='midlo',
            old_name='say1',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='recentworks',
            old_name='cmpny1',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='recentworks',
            old_name='rw1',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='recentworks',
            old_name='website1',
            new_name='website',
        ),
        migrations.RemoveField(
            model_name='mid',
            name='mimg',
        ),
        migrations.RemoveField(
            model_name='midlo',
            name='im1',
        ),
        migrations.RemoveField(
            model_name='text1',
            name='desc',
        ),
        migrations.AddField(
            model_name='mid',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images'),
        ),
        migrations.AddField(
            model_name='midlo',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images'),
        ),
        migrations.AddField(
            model_name='text1',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name=b'description', blank=True),
        ),
        migrations.AlterField(
            model_name='homesliderimages1',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name=b'description', blank=True),
        ),
        migrations.AlterField(
            model_name='homesliderimages1',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name=b'title', blank=True),
        ),
        migrations.AlterField(
            model_name='text1',
            name='boldtitle',
            field=models.CharField(max_length=255, null=True, verbose_name=b'boldtitle', blank=True),
        ),
        migrations.AlterField(
            model_name='text1',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name=b'text', blank=True),
        ),
        migrations.AlterField(
            model_name='text2',
            name='boldtitle',
            field=models.CharField(max_length=255, null=True, verbose_name=b'boldtitle', blank=True),
        ),
        migrations.AlterField(
            model_name='text2',
            name='desc',
            field=models.CharField(max_length=255, null=True, verbose_name=b'description', blank=True),
        ),
        migrations.AlterField(
            model_name='text2',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name=b'text', blank=True),
        ),
    ]
