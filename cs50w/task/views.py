from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="add task")


# Create your views here.

#tasks = ["mango", "banana", "orange"]

def index(request):
    if "tasks" not in request.session:
        request.session['tasks'] = []

    return render(request, "index.html", {
        "tasks": request.session['tasks']
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request, 'add.html', {
                "form": form
            })
    return render(request, "add.html", {
        "form": NewTaskForm()
    })