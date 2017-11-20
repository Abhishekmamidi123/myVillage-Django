from django.conf.urls import url, include
from django.contrib import admin
from . import views

# including map name to use it in templates.
app_name = 'predict'

# Sub urls for predict app
urlpatterns = [
    # predicting weather trends
    url(r'^weather/$', views.weather, name='weather'),
    # predicting market prices
    url(r'^market/', views.market, name='market'),
]
