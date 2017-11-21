# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

admin.site.register(models.house)
admin.site.register(models.member)
admin.site.register(models.housePhoto)
admin.site.register(models.houseAudio)
admin.site.register(models.farm)
admin.site.register(models.point)
admin.site.register(models.crop)
admin.site.register(models.season)
admin.site.register(models.cropping)
admin.site.register(models.farmPhoto)
admin.site.register(models.farmAudio)
admin.site.register(models.well)
admin.site.register(models.dateTime)
admin.site.register(models.wellPhoto)
admin.site.register(models.wellAudio)
admin.site.register(models.graphColors)
admin.site.register(models.weather)

