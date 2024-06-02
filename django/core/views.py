from django.shortcuts import render
from django.http import HttpResponse 
from django.views import View


# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing/index.html")