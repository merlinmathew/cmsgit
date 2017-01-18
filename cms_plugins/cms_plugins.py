from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import About , Testimonial , HomeSliderImages1 , Text1, Text2, BottomLogos, RecentWorks, Mid , MidLo
from django.contrib import admin
__author__ = 'user'

class AboutP(CMSPluginBase):

    model = About
    name = _('About')
    render_template = 'npl_about.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

class HomePlugin(CMSPluginBase):

    model = Testimonial
    name = _('Testimonial')
    render_template = 'testimonial.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

class HomeSliderImages1Plugin(CMSPluginBase):

    model = HomeSliderImages1
    name = _('Banner')
    render_template = 'homesliderimages1.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

class Text1Plugin(CMSPluginBase):

    model = Text1
    name = _('Text1')
    render_template = 'text1.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

class Text2Plugin(CMSPluginBase):

    model = Text2
    name = _('Text2')
    render_template = 'text2.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

class BottomLogosPlugin(CMSPluginBase):

    model = BottomLogos
    name = _('BottomLogos')
    render_template = 'bottomlogos.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

class RecentWorksPlugin(CMSPluginBase):

    model = RecentWorks
    name = _('RecentWorks')
    render_template = 'recentworks.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

class MidPlugin(CMSPluginBase):

    model = Mid
    name = _('Mid')
    render_template = 'mid.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

class MidLoPlugin(CMSPluginBase):

    model = MidLo
    name = _('MidLogos')
    render_template = 'midlo.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(AboutP)
plugin_pool.register_plugin(HomePlugin)
plugin_pool.register_plugin(HomeSliderImages1Plugin)
plugin_pool.register_plugin(Text1Plugin)
plugin_pool.register_plugin(Text2Plugin)
plugin_pool.register_plugin(BottomLogosPlugin)
plugin_pool.register_plugin(RecentWorksPlugin)
plugin_pool.register_plugin(MidPlugin)
plugin_pool.register_plugin(MidLoPlugin)