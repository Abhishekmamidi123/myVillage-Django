# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# including modules
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . import models
from .forms import YearForm
import json
import urllib2
import datetime
from django.template import loader
from django.http import HttpResponse

# view for house gallery
def gallery(request, pk):
    ''' This view returns the list of photos of the selected house and the house id '''
    url="http://10.0.3.23:2729/housePhoto"
    json_obj=urllib2.urlopen(url)
    photolist = json.load(json_obj)
    photolist1=[]
    # filtering photoList of that house
    for obj in photolist:
        if obj['house'] == int(pk):
            photolist1.append('http://10.0.3.23:2729'+obj['photo'].encode('ascii', 'ignore'))
    return render(request, "map/detail_gallery.html", {'loop_times':range(0, len(photolist1)), 'pk':pk, 'photolist':photolist1 })

# view for house audio
def audio(request, pk):
    ''' This view returns the list of audio clips of the selected house and the house id '''
    url="http://10.0.3.23:2729/houseAudio"
    json_obj=urllib2.urlopen(url)
    audiolist = json.load(json_obj)
    audiolist1=[]
    # filtering audioList of that house
    for obj in audiolist:
        if obj['house'] == int(pk):
            audiolist1.append('http://10.0.3.23:2729'+obj['audio'].encode('ascii', 'ignore'))
    return render(request, "map/detail_audio.html", {'loop_times':range(0, len(audiolist1)), 'pk':pk, 'audiolist':audiolist1 })

# view for house video
def video(request, pk):
    ''' This view returns the list of video clips of the selected house and the house id '''
    return render(request, "map/detail_video.html", {'pk':pk})

# Shows the houses on the map
def HouseList(request):
    ''' returns the house attributes retrieved from REST API '''
    url="http://10.0.3.23:2729/house/"
    json_obj=urllib2.urlopen(url)
    houselist=json.load(json_obj)
    # Initialising lists
    latlon=[]
    idList = []
    members=[]
    income=[]
    # Storing the atributes in the corresponding lists
    for i in houselist:
    	latlon.append(i['lat'])
    	latlon.append(i['lon'])
        latlon.append(int(i['id']))
        idList.append(int(i['id']))
        members.append(i['members'])
        income.append(i['income'])
    # Passing the lists to the template
    context={'houselist':json.dumps(houselist),'latlon':latlon,'idList':idList,'members':members,"income":income}
    return render(request,'map/maps.html',context)

# view for the 3D Visualization of the wells on the map
def WellsList(request):
    ''' returns the well attributes retrieved from REST API '''
    url="http://10.0.3.23:2729/wells/"
    json_obj=urllib2.urlopen(url)
    welllist=json.load(json_obj)
    # Initialising lists
    w=[]
    l=[]
    d=[]
    w=[]
    # Storing the atributes in the corresponding lists
    for i in welllist:
    	l.append(i['lat'])
    	l.append(i['lon'])
        d.append(i['depth'])
        w.append(i['averageWaterYield'])
    # Passing the lists to the template
    context={'welllist':json.dumps(welllist),'latlon':l,'depth':d,'water':w}
    return render(request,'map/map_wells.html',context)

# view for showing the houses on the map
def FarmsList(request):
    ''' returns the well attributes retrieved from REST API '''
    url1="http://10.0.3.23:2729/farm/"
    url2="http://10.0.3.23:2729/point/"
    json_obj1=urllib2.urlopen(url1)
    json_obj2=urllib2.urlopen(url2)
    farmlist=json.load(json_obj1)
    pointlist=json.load(json_obj2)
    # Initialising lists
    l=[]
    j=0
    # Storing the atributes in the corresponding lists
    for i in pointlist:
    	l.append(i['lat'])
    	l.append(i['lon'])
        j=j+2
        if(j==8):
            l.append(i['farm'])
            j=0
    # Retrieving farm json object from the server
    url1="http://10.0.3.23:2729/farm"
    json_obj1=urllib2.urlopen(url1)
    farmList=json.load(json_obj1)
    # Retrieving cropping json object from the server
    url2="http://10.0.3.23:2729/cropping/"
    json_obj2=urllib2.urlopen(url2)
    croppingList=json.load(json_obj2)
    dic={}
    for i in range(len(farmList)):
        dic[i]=[]
    # Calculating the current year and season
    now=datetime.datetime.now()
    year=now.year
    month=now.month
    if month>=7 and month<10:
		season_id = 1   #kharif
    elif month>=10 and month<3:
		season_id = 2 # rabi
    else:
		season_id = 3 # summer
    cropList=[]
    for i in croppingList:
        if i['season'] == season_id and i['year'] == str(year):
            dic[i['farm']-1].append(i['crop'])
            dic[i['farm']-1].append(i['area'])
    # Passing the lists to the template
    context={"farmlist":json.dumps(farmlist),'pointlist':json.dumps(pointlist),'latlon':l,'dic':dic}
    return render(request,'map/map_farms.html',context)

# Not required
def farmHistory(request, pk):
    url="http://10.0.3.23:2729/cropping"
    json_obj=urllib2.urlopen(url)
    farmHistoryList = json.load(json_obj)
    farmList=[]
    now=datetime.datetime.now()
    year = now.year
    for obj in farmHistoryList:
        if obj['farm'] == int(pk):
            if obj['year'] == str(year):
                dic=[]
                dic.append(obj['area'])
                dic.append(obj['crop'])
                dic.append(obj['season'])
                farmList.append(dic)
    context={'farmlist':farmList,'pk':pk}
    # photolist1 = [obj['photo'].encode('ascii', 'ignore') for obj in photolist if(obj['house'] == int(pk))]
    return render(request, "map/farmHistory.html",context)

# view for Visualization of year wise farm history on the map
def farmHistoryYear(request, pk):
    ''' returns the year specific farm attributes attributes retrieved from REST API '''
    url="http://10.0.3.23:2729/cropping"
    json_obj=urllib2.urlopen(url)
    farmHistoryList = json.load(json_obj)
    farmList=[]
    # if - If year is entered (POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        empty_form = YearForm()
        form = YearForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            flag=0
            for obj in farmHistoryList:
                if obj['farm'] == int(pk):
                    if obj['year'] == request.POST.get('year'):
                        dic=[]
                        dic.append(obj['area'])
                        dic.append(obj['crop'])
                        dic.append(obj['season'])
                        farmList.append(dic)
                        flag=1
            #process the data in form.cleaned_data as required
            locationGo = "/farmHistory/"
            template = loader.get_template("map/farmHistory.html")
            return HttpResponse(template.render({'farmList':farmList,'form':empty_form,'flag':flag},request))
    # If the year is not entered in the form. It shows the current year analysis.
    else:
            now=datetime.datetime.now()
            year=now.year
            flag=0
            for obj in farmHistoryList:
                if obj['farm'] == int(pk):
                    if obj['year'] == str(year):
                        dic=[]
                        dic.append(obj['area'])
                        dic.append(obj['crop'])
                        dic.append(obj['season'])
                        farmList.append(dic)
                        flag=1
            form = YearForm()
            template = loader.get_template("map/farmHistory.html")
            context = {'form': form,'farmList':farmList,'flag':flag}
    return HttpResponse(template.render(context, request))

# View for showing overview of farms, wells and houses on the map of the village.
def OverViewList(request):
    ''' returns attributes of houses, wells and farms '''
    url="http://10.0.3.23:2729/house/"
    json_obj=urllib2.urlopen(url)
    houselist=json.load(json_obj)
    latlon1=[]
    for i in houselist:
    	latlon1.append(i['lat'])
    	latlon1.append(i['lon'])
        latlon1.append(int(i['id']))

    url="http://10.0.3.23:2729/wells/"
    json_obj=urllib2.urlopen(url)
    welllist=json.load(json_obj)
    l2=[]
    for i in welllist:
    	l2.append(i['lat'])
    	l2.append(i['lon'])

    url1="http://10.0.3.23:2729/farm/"
    url2="http://10.0.3.23:2729/point/"
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

# Not required
def WellVisualize(request):
    url1="http://10.0.3.23:2729/wells/"
    json_obj1=urllib2.urlopen(url1)
    wellsList=json.load(json_obj1)

    url2="http://10.0.3.23:2729/dateTime/"
    json_obj2=urllib2.urlopen(url2)
    dateTimeList=json.load(json_obj2)

    context = {'wellslist':wellslist, 'dateTimeList':dateTimeList}
    return render(request,'#',context)

def wellHistory(request, pk):
    url1="http://10.0.3.23:2729/dateTime"
    json_obj1=urllib2.urlopen(url1)
    wellsList=json.load(json_obj1)
    recentHistoryList=[]
    cnt=0
    # for i in wellsList[::-1]:
    for i in wellsList:
        if i['well']==pk:
    		if cnt==7:
    			break
    		else:
    			recentHistoryList.append(i['wateryield'])
    			cnt+=1
    context = {'recentHistoryList':recentHistoryList,'pk':pk}
    return render(request,'map/wellHistory.html',context)

# view for Visualization of crop statistics in farms using pie chart
def FarmVisualize(request):
    url1="http://10.0.3.23:2729/farm"
    json_obj1=urllib2.urlopen(url1)
    farmList=json.load(json_obj1)

    url2="http://10.0.3.23:2729/cropping/"
    json_obj2=urllib2.urlopen(url2)
    croppingList=json.load(json_obj2)

    dic={}
    for i in range(len(farmList)):
        dic[i]=[]

    # Retrieving current year and season
    now=datetime.datetime.now()
    year=now.year
    month=now.month
    if month>=7 and month<10:
		season_id = 1   #kharif
    elif month>=10 and month<3:
		season_id = 2 # rabi
    else:
		season_id = 3 # summer
    cropList=[]
    # Crop wise attributes for the current year and season (which is dynamic)
    for i in croppingList:
        if i['season'] == season_id and i['year'] == str(year):
            if i['crop']==1:
                dic[i['farm']-1].append("Paddy")
                dic[i['farm']-1].append(i['area'])
            elif(i['crop']==2):
                dic[i['farm']-1].append("Corn")
                dic[i['farm']-1].append(i['area'])
            if(i['crop']==3):
                dic[i['farm']-1].append("Wheat")
                dic[i['farm']-1].append(i['area'])
            if(i['crop']==4):
                dic[i['farm']-1].append("Jute")
                dic[i['farm']-1].append(i['area'])
            if(i['crop']==5):
                dic[i['farm']-1].append("Tomato")
                dic[i['farm']-1].append(i['area'])
            if(i['crop']==6):
                dic[i['farm']-1].append("Onion")
                dic[i['farm']-1].append(i['area'])
            if(i['crop']==7):
                dic[i['farm']-1].append("Coton")
                dic[i['farm']-1].append(i['area'])

    context = {'farmList':farmList, 'cropList':cropList,'dic':dic}
    return render(request,'',context)
