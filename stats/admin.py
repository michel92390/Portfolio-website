# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Stat

# Register your models here
class StatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'how_many')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_per_page = 20


admin.site.register(Stat, StatsAdmin)