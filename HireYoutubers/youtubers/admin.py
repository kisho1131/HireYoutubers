from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html


# Register your models here.
class YTubers(admin.ModelAdmin):
    def ProfilePhoto(self, object):
        return format_html('<img src = "{}" width = "40px" height = "40px" style = "border-radius: 50%"/>'.format(object.photo.url))
    list_display = ('id', 'name', 'ProfilePhoto', 'subs_count')
    list_display_links = ('name', 'subs_count')
    list_filter = ('city', 'camera_type')

admin.site.register(Youtuber, YTubers)
