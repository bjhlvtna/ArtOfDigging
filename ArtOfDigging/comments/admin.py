#-*- coding: utf-8 -*-

from models import *
from django.contrib import admin

class MarkdownCommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'content_type', 'content_object', 'user_name', 'user_email', 'user_url', 'is_public', 'submit_date')

admin.site.register(MarkdownComment, MarkdownCommentAdmin)