from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'get_html_photo', 'time_create')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_filter = ('time_create', )
    prepopulated_fields = {"slug": ("name",)}
    fields = ('name', 'slug', 'cat', 'price', 'photo', 'get_html_photo', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Photos"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)