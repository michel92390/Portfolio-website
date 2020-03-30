# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import About

# Register your models here
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'photo_main')
    list_display_links = ('id', 'name')
    list_per_page = 20


admin.site.register(About, AboutAdmin)