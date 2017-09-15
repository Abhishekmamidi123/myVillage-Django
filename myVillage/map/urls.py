from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'map'

urlpatterns = [
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^audio/', views.audio, name='audio'),
    url(r'^video/', views.video, name='video'),
    url(r'^households/', views.HouseList, name='households'),
    url(r'^wells/', views.WellsList, name='wells'),
    url(r'^farms/', views.FarmsList, name='farms'),
    url(r'^overview/', views.OverViewList, name='overall'),
]
