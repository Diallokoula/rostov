from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "home.html"

class AboutPage(TemplateView):
    template_name = "about.html"