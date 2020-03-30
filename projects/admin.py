# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project

# Register your models here
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'types', 'is_published', 'photo_main')
    list_display_links = ('id', 'title')
    list_filter = ('name',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'list_date', 'website')
    list_per_page = 20


admin.site.register(Project, ProjectAdmin)
