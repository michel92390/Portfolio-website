# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Skill

# Register your models here
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'pourcentage', 'is_published', 'list_date')
    list_display_links = ('id', 'language')
    list_editable = ('is_published',)
    list_per_page = 20


admin.site.register(Skill, SkillsAdmin)
