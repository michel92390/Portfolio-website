# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Skill(models.Model):
    language = models.CharField(max_length=200)
    pourcentage = models.IntegerField()
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
