# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from . import models
import json
import urllib2

class Gallery(TemplateView):
    template_name = "map/detail_gallery.html"

def audio(request):
    return render(request, "map/detail_audio.html", None)

def video(request):
    return render(request, "map/detail_video.html", None)

# def map(request):
#     return render(request, 'map/maps.html', None)

def HouseList(request):
    url="http://restserver123.pythonanywhere.com/house/"
    json_obj=urllib2.urlopen(url)
    houselist=json.load(json_obj)
    return render(request,'map/maps.html',{"houselist":json.dumps(houselist)})

def WellsList(request):
    url="http://restserver123.pythonanywhere.com/house/"
    json_obj=urllib2.urlopen(url)
    houselist=json.load(json_obj)
    return render(request,'map/map_wells.html',{"houselist":json.dumps(houselist)})

def FarmsList(request):
    url="http://restserver123.pythonanywhere.com/house/"
    json_obj=urllib2.urlopen(url)
    houselist=json.load(json_obj)
    return render(request,'map/map_farms.html',{"houselist":json.dumps(houselist)})

def OverViewList(request):
    url="http://restserver123.pythonanywhere.com/house/"
    json_obj=urllib2.urlopen(url)
    houselist=json.load(json_obj)
    return render(request,'map/map_overview.html',{"houselist":json.dumps(houselist)})

# class HouseList(ListView):
#     model = models.house
#     template_name = "map/maps.html"
#     context_object_name = "houselist"
