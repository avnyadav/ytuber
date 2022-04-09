from django.contrib import admin
from .models import Slider,Team
# Register your models here.
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    def myphoto(self,object):
        return format_html('<img  width="40" src="{}" />'.format(object.photo.url))

    list_display = ("id","myphoto","first_name","role","created_date")
    list_display_links = ('first_name','id',)
    search_fields = ('first_name','role',)
    list_filter = ('role',)


admin.site.register(Slider)
admin.site.register(Team,TeamAdmin)




