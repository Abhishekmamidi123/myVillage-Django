# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
