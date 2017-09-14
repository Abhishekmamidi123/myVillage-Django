from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView


class Test(TemplateView):
    template_name = "base.html"

class HomePage(TemplateView):
    template_name = "index.html"
