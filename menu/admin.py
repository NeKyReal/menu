from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 1


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent')
    list_filter = ('menu',)
    search_fields = ('title',)
