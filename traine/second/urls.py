from django.urls import path
from . import views

urlpatterns = [
    path("", views.second, name="second"),
    path("second", views.first, name="first")
]