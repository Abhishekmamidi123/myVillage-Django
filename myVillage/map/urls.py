from django.conf.urls import url, include
from django.contrib import admin
from . import views

# including map name to use it in templates.
app_name = 'map'

# Sub urls for map app
urlpatterns = [
    # house gallery
    url(r'^gallery/(?P<pk>[0-9]+)/$', views.gallery, name='gallery'),
    # house audio
    url(r'^audio/(?P<pk>[0-9]+)/$', views.audio, name='audio'),
    # house video
    url(r'^video/(?P<pk>[0-9]+)/$', views.video, name='video'),
    # households
    url(r'^households/', views.HouseList, name='households'),
    # wells
    url(r'^wells/', views.WellsList, name='wells'),
    # wellHistory
    url(r'^wellHistory/(?P<pk>[0-9]+)/$', views.wellHistory, name='wellHistory'),
    # farms
    url(r'^farms/', views.FarmsList, name='farms'),
    # farmHistory
    url(r'^farmHistory/(?P<pk>[0-9]+)/$', views.farmHistory, name='farmHistory'),
    # Year wise farmHistory
    url(r'^farmHistoryYear/(?P<pk>[0-9]+)/$', views.farmHistoryYear, name='farmHistoryYear'),
    # village overview
    url(r'^overview/', views.OverViewList, name='overall'),
]
