from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import first
# Create your views here.
def second(request):
    return render(request, "second.html")


from django.http import HttpResponse
from django.shortcuts import render
import os

def download_file(request, filename):
    file_path = os.path.join('path_to_files', filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        return HttpResponse("File not found.")
