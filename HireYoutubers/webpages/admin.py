from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def ProfilePhoto(self, object):
        return format_html('<img src = "{}" width = "40px" height = "40px" style = "border-radius: 50%"/>'.format(object.photo.url))
    list_display = ('id', 'ProfilePhoto','first_name', 'role', 'created_date')
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'role')
    list_filter = ('role',)


admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)