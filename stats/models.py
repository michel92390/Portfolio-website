# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Stat(models.Model):
    title = models.TextField(max_length=200)
    is_published = models.BooleanField(default=True)
    how_many = models.IntegerField()
   
