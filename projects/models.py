# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from datetime import datetime
from about.models import About




# Create your models here.
class Project(models.Model):
    name = models.ForeignKey(About, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    types = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    website = models.URLField(max_length = 200)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
