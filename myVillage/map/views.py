# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from . import models
import json
import urllib2
import datetime

def gallery(request, pk):
    url="http://10.0.3.23:1111/housePhoto"
    json_obj=urllib2.urlopen(url)
    photolist = json.load(json_obj)
    photolist1=[]
    for obj in photolist:
        if obj['house'] == int(pk):
            photolist1.append('http://10.0.3.23:1111'+obj['photo'].encode('ascii', 'ignore'))
    # photolist1 = [obj['photo'].encode('ascii', 'ignore') for obj in photolist if(obj['house'] == int(pk))]
    return render(request, "map/detail_gallery.html", {'loop_times':range(0, len(photolist1)), 'pk':pk, 'photolist':photolist1 })

def audio(request, pk):
    # return render(request, "map/detail_audio.html", {'pk': pk})
    url="http://10.0.3.23:1111/houseAudio"
    json_obj=urllib2.urlopen(url)
    audiolist = json.load(json_obj)
    audiolist1=[]
    for obj in audiolist:
        if obj['house'] == int(pk):
            audiolist1.append('http://10.0.3.23:1111'+obj['audio'].encode('ascii', 'ignore'))
    return render(request, "map/detail_audio.html", {'loop_times':range(0, len(audiolist1)), 'pk':pk, 'audiolist':audiolist1 })

def video(request, pk):
    return render(request, "map/detail_video.html", {'pk':pk})

# def map(request):
#     return render(request, 'map/maps.html', None)

def HouseList(request):
    url="http://10.0.3.23:1111/house/"
    json_obj=urllib2.urlopen(url)
    houselist=json.load(json_obj)
    latlon=[]
    idList = []
    for i in houselist:
    	latlon.append(i['lat'])
    	latlon.append(i['lon'])
        latlon.append(int(i['id']))
        idList.append(int(i['id']))
    context={'houselist':json.dumps(houselist),'latlon':latlon,'idList':idList}
    return render(request,'map/maps.html',context)

def WellsList(request):
    url="http://10.0.3.23:1111/wells/"
    json_obj=urllib2.urlopen(url)
    welllist=json.load(json_obj)
    l=[]
    for i in welllist:
    	l.append(i['lat'])
    	l.append(i['lon'])
    context={'welllist':json.dumps(welllist),'latlon':l}
    return render(request,'map/map_wells.html',context)

def FarmsList(request):
    url1="http://10.0.3.23:1111/farm/"
    url2="http://10.0.3.23:1111/point/"
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
    url="http://10.0.3.23:1111/house/"
    json_obj=urllib2.urlopen(url)
    houselist=json.load(json_obj)
    latlon1=[]
    for i in houselist:
    	latlon1.append(i['lat'])
    	latlon1.append(i['lon'])
        latlon1.append(int(i['id']))

    url="http://10.0.3.23:1111/wells/"
    json_obj=urllib2.urlopen(url)
    welllist=json.load(json_obj)
    l2=[]
    for i in welllist:
    	l2.append(i['lat'])
    	l2.append(i['lon'])

    url1="http://10.0.3.23:1111/farm/"
    url2="http://10.0.3.23:1111/point/"
    json_obj1=urllib2.urlopen(url1)
    json_obj2=urllib2.urlopen(url2)
    farmlist=json.load(json_obj1)
    pointlist=json.load(json_obj2)
    l3=[]
    for i in pointlist:
    	l3.append(i['lat'])
    	l3.append(i['lon'])

    context={'houselist':json.dumps(houselist),'latlon':latlon1, 'welllist':json.dumps(welllist),'latlon2':l2, "farmlist":json.dumps(farmlist),'pointlist':json.dumps(pointlist),'latlon3':l3}
    return render(request,'map/map_overview.html',context)

def WellVisualize(request):
	url1="http://10.0.3.23:1111/wells/"
    json_obj1=urllib2.urlopen(url1)
    wellsList=json.load(json_obj1)

    url2="http://10.0.3.23:1111/dateTime/"
    json_obj2=urllib2.urlopen(url2)
    dateTimeList=json.load(json_obj2)
	
    context = {'wellslist':wellslist, 'dateTimeList':dateTimeList}
    return render(request,'#',context)
    
def WellHistory(request, pk):
	url1="http://10.0.3.23:1111/dateTime/pk"
    json_obj1=urllib2.urlopen(url1)
    wellsList=json.load(json_obj1)
    recentHistoryList=[]
	cnt=0
	for i in wellsList[::-1]:
		if cnt==7:
			break
		else:
			recentHistoryList.append(i)
			cnt+=1
	context = {'farmList':farmList, 'cropList':cropList}
    return render(request,'#',context)

def FarmVisualize(request):
	url1="http://10.0.3.23:1111/farm/"
    json_obj1=urllib2.urlopen(url1)
    farmList=json.load(json_obj1)

    url2="http://10.0.3.23:1111/cropping/"
    json_obj2=urllib2.urlopen(url2)
    croppingList=json.load(json_obj2)
	
	now=datetime.datetime.now()
	year = now.year
	month = now.month
	
	if month>=7 and month<10:
		season_id = 1 # kharif
	else if month>=10 and month<3:
		season_id = 2 # rabi
	else:
		season_id = 3 # summer
	
	cropList=[]
	for i in croppingList:
		if i['season'] == season_id and i['year'] == str(year):
			cropList.append(i)
	
	context = {'farmList':farmList, 'cropList':cropList}
    return render(request,'#',context)

def 
 
