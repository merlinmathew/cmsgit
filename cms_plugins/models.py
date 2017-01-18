# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from django.contrib.sites.models import Site

class About(CMSPlugin):
    # your fields
    about_text = models.CharField('About', max_length=255, null=True, blank=True)

class Testimonial(CMSPlugin):
    # your fields
    testimonial = models.CharField('testimonial', max_length=255, null=True, blank=True)
    name = models.CharField('name', max_length=255, null=True, blank=True)
    company = models.CharField('company',max_length=255, null=True, blank=True)

class HomeSliderImages1(CMSPlugin):
    bannerimage = models.ImageField(upload_to="sliderimages", null=True)
    title = models.CharField('title', max_length=255, null=True, blank=True)
    description = models.CharField('description', max_length=255, null=True, blank=True)

class Text1(CMSPlugin):
    # your fields
    title = models.CharField('text', max_length=255, null=True, blank=True)
    boldtitle = models.CharField('boldtitle', max_length=255, null=True, blank=True)
    description = models.CharField('description', max_length=255, null=True, blank=True)

class Text2(CMSPlugin):
    # your fields
    title = models.CharField('text', max_length=255, null=True, blank=True)
    boldtitle = models.CharField('boldtitle', max_length=255, null=True, blank=True)
    desc = models.CharField('description', max_length=255, null=True, blank=True)

class BottomLogos(CMSPlugin):
    # your fields
    image = models.ImageField(upload_to="bottomlogos",null=True)

class RecentWorks(CMSPlugin):
    # your fields
    image = models.ImageField(upload_to="work",null=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)

class Mid(CMSPlugin):
    # your fields
    image = models.ImageField(upload_to="images",null=True)
    number1 = models.CharField(max_length=255, null=True, blank=True)
    description1 = models.CharField(max_length=255, null=True, blank=True)
    number2 = models.CharField(max_length=255, null=True, blank=True)
    description2 = models.CharField(max_length=255, null=True, blank=True)
    number3 = models.CharField(max_length=255, null=True, blank=True)
    description3 = models.CharField(max_length=255, null=True, blank=True)
    number4 = models.CharField(max_length=255, null=True, blank=True)
    description4 = models.CharField(max_length=255, null=True, blank=True)

class MidLo(CMSPlugin):
    # your fields
    image = models.ImageField(upload_to="images",null=True)
    description = models.CharField(max_length=255, null=True, blank=True)
