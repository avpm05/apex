# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BlogPosts,Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','created','active')
    list_filter = ('active','created','updated')
    search_fileds = ('name','email','body')

admin.site.register(Comment,CommentAdmin)
