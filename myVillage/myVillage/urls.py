"""myVillage URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

# main urls of our website
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),  # admin page
    url(r'^map/', include('map.urls')), # maps app
    url(r'^farmers/', include('farmers.urls')),  # framers app
    url(r'^school/', include('school.urls')),  # school app
    url(r'^social/', include('social.urls')),  # social app
    url(r'^$', views.HomePage.as_view(), name="home"),  # Home page
    url(r'^main/$', views.Test.as_view(), name="test"), # tests page
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)   # including URL's of static files
urlpatterns = format_suffix_patterns(urlpatterns, False, allowed=['json', 'html'])
