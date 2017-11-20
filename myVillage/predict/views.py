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
    url="http://10.0.3.23:2729/weather"
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
    predicted_value = os.popen('python holtWinter.py "' + temp  + '"').read()[:-1]
    tomorrow = str(datetime.datetime.strptime(dates[len(dates)-1][2:], '%y-%m-%d').date() + datetime.timedelta(days=1))
    dates.append(tomorrow)
    temperature.append(predicted_value)
    print dates
    print temperature
    return render(request, "predict/weather.html", {'dates':dates, 'temperature':temperature})

def market(request):
	return HttpResponse("hello")

