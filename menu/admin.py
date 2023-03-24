from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent', 'order', )
    fields = ['name', 'url', 'parent', 'order', ]


admin.site.register(Menu, MenuAdmin)
