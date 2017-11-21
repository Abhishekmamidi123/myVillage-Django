"""rest_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from server import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^house/', views.houseList.as_view()),
    url(r'^house/(?P<pk>[0-9]+)$', views.houseDetail.as_view()),
    url(r'^member/', views.memberList.as_view()),
    url(r'^housePhoto/', views.housePhotoList.as_view()),
    url(r'^houseAudio/', views.houseAudioList.as_view()),
    url(r'^farm/', views.farmList.as_view()),
    url(r'^point/', views.pointList.as_view()),
    url(r'^crop/', views.cropList.as_view()),
    url(r'^season/', views.seasonList.as_view()),
    url(r'^cropping/', views.croppingList.as_view()),
    url(r'^farmPhoto/', views.farmPhotoList.as_view()),
    url(r'^farmAudio/', views.farmAudioList.as_view()),
    url(r'^wells/', views.wellList.as_view()),
    url(r'^dateTime/', views.dateTimeList.as_view()),
    url(r'^wellPhoto/', views.wellPhotoList.as_view()),
    url(r'^wellAudio/', views.wellAudioList.as_view()), 
    url(r'graphColors/', views.graphColorsList.as_view()),   
    url(r'weather/', views.weatherList.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns, False, allowed=['json', 'html'])

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
