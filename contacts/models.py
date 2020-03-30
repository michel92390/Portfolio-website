# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    message = models.TextField(blank=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
