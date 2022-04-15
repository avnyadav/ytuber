from django.contrib import admin
from .models import HireTubers
# Register your models here.
from django.utils.html import format_html
from youtubers.models import Youtuber
from django.contrib.auth.models import User

class HireTubersAdmin(admin.ModelAdmin):
    def user_name(self,object):
        user = User.objects.get(id=object.user_id)
        return format_html(f"<a href='/admin/auth/user/{user.id}/change/'>{user.first_name} {user.last_name}</a>")
    def tuber_name(self,object):
        youtuber = Youtuber.objects.get(id=object.id)
        
        return format_html(f"<a href='/admin/youtubers/youtuber/{youtuber.id}/change/'>{youtuber.name} </a>")
    list_display = ("id","first_name","last_name","tuber_name","user_name","created_date")

    





admin.site.register(HireTubers,HireTubersAdmin)