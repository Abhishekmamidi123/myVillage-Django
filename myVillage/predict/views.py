# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . import models
import json
import urllib2
import datetime
from django.template import loader
from django.http import HttpResponse
import os


def weather(request):
    url="http://10.0.3.23:2728/weather"
    json_obj=urllib2.urlopen(url)
    weatherlist = json.load(json_obj)
    dates = []
    temperature = []
    for obj in weatherlist:
    	dates.append(obj['date'])
    	temperature.append(obj['temperature'])
    	temp = ''
    	for x in temperature:
			temp+=str(x)+' '
    predicted_value = os.popen('python predict/holtWinter.py "' + temp  + '"').read()[:-1]
    print predicted_value
    tomorrow = str(datetime.datetime.strptime(dates[len(dates)-1][2:], '%y-%m-%d').date() + datetime.timedelta(days=1))
    dates.append(tomorrow)
    temperature.append(round(float(predicted_value),2))
    print len(dates)
    print len(temperature)
    data = []
    for i in range(len(dates)):
		temp = {}
		temp['date'] = dates[i]
		temp['value'] = temperature[i]
		if i==len(dates)-2:
			temp['dashLengthLine'] = 5
		if i==len(dates)-1:
			temp['dashLengthLine'] = 5
			temp['additional'] = '(Predicted)'				
		data.append(temp)
    return render(request, "predict/weather.html", {'data':json.dumps(data)})

def market(request):
    # url="http://10.0.3.23:2728/market"
    # json_obj=urllib2.urlopen(url)
    # marketlist = json.load(json_obj)
    # data = []
    # for obj in marketlist:
    #	temp = {}
    #	temp['year'] = obj['year']
    #	temp['onion'] = obj['onion']
    #	temp['chilli'] = obj['chilli']
    #	temp['tomato'] = obj['tomato']
    #	temp['cotton'] = obj['cotton']
    # onion, tomato, chilli, cotton
    return render(request, "predict/market.html", {'data':'hello'})

