# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from . import models
import json
import urllib2

def gallery(request, pk):
    return render(request, "map/detail_gallery.html", {'loop_times':range(1, 4), 'pk':pk})

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
    latlon=[]
    idList = []
    for i in houselist:
    	latlon.append(i['lat'])
    	latlon.append(i['lon'])
        latlon.append(i['id'])
        idList.append(i['id'])
    context={'houselist':json.dumps(houselist),'latlon':latlon,'idList':idList}
    return render(request,'map/maps.html',context)

def WellsList(request):
    url="http://restserver123.pythonanywhere.com/wells/"
    json_obj=urllib2.urlopen(url)
    welllist=json.load(json_obj)
    l=[]
    for i in welllist:
    	l.append(i['lat'])
    	l.append(i['lon'])
    context={'welllist':json.dumps(welllist),'latlon':l}
    return render(request,'map/map_wells.html',context)

def FarmsList(request):
    url1="http://restserver123.pythonanywhere.com/farm/"
    url2="http://restserver123.pythonanywhere.com/point/"
    json_obj1=urllib2.urlopen(url1)
    json_obj2=urllib2.urlopen(url2)
    farmlist=json.load(json_obj1)
    pointlist=json.load(json_obj2)
    l=[]
    for i in pointlist:
    	l.append(i['lat'])
    	l.append(i['lon'])
    context={"farmlist":json.dumps(farmlist),'pointlist':json.dumps(pointlist),'latlon':l}
    return render(request,'map/map_farms.html',context)


def OverViewList(request):
    url="http://restserver123.pythonanywhere.com/house/"
    json_obj=urllib2.urlopen(url)
    houselist=json.load(json_obj)
    return render(request,'map/map_overview.html',{"houselist":json.dumps(houselist)})

# class HouseList(ListView):
#     model = models.house
#     template_name = "map/maps.html"
#     context_object_name = "houselist"
