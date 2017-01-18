# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins', '0007_auto_20170112_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homem',
            old_name='company',
            new_name='company1',
        ),
        migrations.RenameField(
            model_name='homem',
            old_name='name',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='homem',
            old_name='testimonial',
            new_name='testimonial1',
        ),
        migrations.RenameField(
            model_name='mid',
            old_name='image',
            new_name='mimg',
        ),
        migrations.RenameField(
            model_name='mid',
            old_name='number',
            new_name='num1',
        ),
        migrations.RenameField(
            model_name='mid',
            old_name='text',
            new_name='num2',
        ),
        migrations.RenameField(
            model_name='midlo',
            old_name='image',
            new_name='im1',
        ),
        migrations.RenameField(
            model_name='midlo',
            old_name='text',
            new_name='say1',
        ),
        migrations.RenameField(
            model_name='recentworks',
            old_name='company',
            new_name='cmpny1',
        ),
        migrations.RenameField(
            model_name='recentworks',
            old_name='website',
            new_name='cmpny2',
        ),
        migrations.RenameField(
            model_name='recentworks',
            old_name='image',
            new_name='rw1',
        ),
        migrations.RemoveField(
            model_name='bottomlogos',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='homesliderimages1',
            name='bannerimage',
        ),
        migrations.RemoveField(
            model_name='homesliderimages1',
            name='description',
        ),
        migrations.RemoveField(
            model_name='homesliderimages1',
            name='title',
        ),
        migrations.RemoveField(
            model_name='text1',
            name='description',
        ),
        migrations.RemoveField(
            model_name='text2',
            name='description',
        ),
        migrations.AddField(
            model_name='bottomlogos',
            name='img1',
            field=models.ImageField(null=True, upload_to=b'bottomlogos'),
        ),
        migrations.AddField(
            model_name='bottomlogos',
            name='img2',
            field=models.ImageField(null=True, upload_to=b'bottomlogos'),
        ),
        migrations.AddField(
            model_name='bottomlogos',
            name='img3',
            field=models.ImageField(null=True, upload_to=b'bottomlogos'),
        ),
        migrations.AddField(
            model_name='bottomlogos',
            name='img4',
            field=models.ImageField(null=True, upload_to=b'bottomlogos'),
        ),
        migrations.AddField(
            model_name='bottomlogos',
            name='img5',
            field=models.ImageField(null=True, upload_to=b'bottomlogos'),
        ),
        migrations.AddField(
            model_name='bottomlogos',
            name='img6',
            field=models.ImageField(null=True, upload_to=b'bottomlogos'),
        ),
        migrations.AddField(
            model_name='homesliderimages1',
            name='desc1',
            field=models.CharField(max_length=255, null=True, verbose_name=b'desc1', blank=True),
        ),
        migrations.AddField(
            model_name='homesliderimages1',
            name='desc2',
            field=models.CharField(max_length=255, null=True, verbose_name=b'desc2', blank=True),
        ),
        migrations.AddField(
            model_name='homesliderimages1',
            name='desc3',
            field=models.CharField(max_length=255, null=True, verbose_name=b'desc3', blank=True),
        ),
        migrations.AddField(
            model_name='homesliderimages1',
            name='slider1',
            field=models.ImageField(null=True, upload_to=b'sliderimages'),
        ),
        migrations.AddField(
            model_name='homesliderimages1',
            name='slider2',
            field=models.ImageField(upload_to=b'sliderimages', null=True, verbose_name='slider image2'),
        ),
        migrations.AddField(
            model_name='homesliderimages1',
            name='slider3',
            field=models.ImageField(upload_to=b'sliderimages', null=True, verbose_name='slider image3'),
        ),
        migrations.AddField(
            model_name='homesliderimages1',
            name='title1',
            field=models.CharField(max_length=255, null=True, verbose_name=b'title1', blank=True),
        ),
        migrations.AddField(
            model_name='homesliderimages1',
            name='title2',
            field=models.CharField(max_length=255, null=True, verbose_name=b'title2', blank=True),
        ),
        migrations.AddField(
            model_name='homesliderimages1',
            name='title3',
            field=models.CharField(max_length=255, null=True, verbose_name=b'title3', blank=True),
        ),
        migrations.AddField(
            model_name='mid',
            name='num3',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mid',
            name='num4',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mid',
            name='wri1',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mid',
            name='wri2',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mid',
            name='wri3',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mid',
            name='wri4',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='midlo',
            name='im2',
            field=models.ImageField(null=True, upload_to=b'mmm'),
        ),
        migrations.AddField(
            model_name='midlo',
            name='im3',
            field=models.ImageField(null=True, upload_to=b'mmm'),
        ),
        migrations.AddField(
            model_name='midlo',
            name='im4',
            field=models.ImageField(null=True, upload_to=b'mmm'),
        ),
        migrations.AddField(
            model_name='midlo',
            name='say2',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='midlo',
            name='say3',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='midlo',
            name='say4',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='recentworks',
            name='cmpny3',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='recentworks',
            name='cmpny4',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='recentworks',
            name='rw2',
            field=models.ImageField(null=True, upload_to=b'work'),
        ),
        migrations.AddField(
            model_name='recentworks',
            name='rw3',
            field=models.ImageField(null=True, upload_to=b'work'),
        ),
        migrations.AddField(
            model_name='recentworks',
            name='rw4',
            field=models.ImageField(null=True, upload_to=b'work'),
        ),
        migrations.AddField(
            model_name='recentworks',
            name='website1',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='recentworks',
            name='website2',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='recentworks',
            name='website3',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='recentworks',
            name='website4',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='text1',
            name='desc',
            field=models.CharField(max_length=255, null=True, verbose_name=b'desc1', blank=True),
        ),
        migrations.AddField(
            model_name='text2',
            name='desc',
            field=models.CharField(max_length=255, null=True, verbose_name=b'desc2', blank=True),
        ),
        migrations.AlterField(
            model_name='text1',
            name='boldtitle',
            field=models.CharField(max_length=255, null=True, verbose_name=b'boldtitle1', blank=True),
        ),
        migrations.AlterField(
            model_name='text1',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name=b'text1', blank=True),
        ),
        migrations.AlterField(
            model_name='text2',
            name='boldtitle',
            field=models.CharField(max_length=255, null=True, verbose_name=b'boldtitle2', blank=True),
        ),
        migrations.AlterField(
            model_name='text2',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name=b'text2', blank=True),
        ),
    ]
