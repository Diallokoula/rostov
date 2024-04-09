from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
# Create your views here.

# tasks = ["banana", "mango", "apple"]
class NewTask(forms.Form):
    name = forms.CharField(label = "add task")

def index(request):
    return HttpResponse("<h1 style='font-size: 80px; text-align: center'>hello world</h1>")

def task(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "task.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data['name']
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("hello:task"))
        else:
            return render(request, "add.html", {
                "form": form
            })
    return render(request, "add.html", {
        "form": NewTask()
    })