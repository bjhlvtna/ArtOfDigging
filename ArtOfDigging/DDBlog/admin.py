#-*- coding: utf-8 -*-

from DDBlog.models import *
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    pass

class FileInline(admin.TabularInline):
    model = File
    extra = 1
    
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [FileInline, ImageInline]
    list_display = ('title', 'publish')
    list_filter = ('publish', 'categories')
    search_fields = ('title', 'body')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)