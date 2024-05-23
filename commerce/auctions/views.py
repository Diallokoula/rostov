from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

from .models import *


def index(request):
    myitems = Product.objects.filter(is_exist = True)
    category = Category.objects.all()
    return render(request, "file/index.html",{
        "items": myitems,
        "category": category
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "file/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "file/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "file/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "file/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "file/register.html")

def createProduct(request):
    if request.method == "GET":
        category = Category.objects.all()
        return render(request, "file/create.html" , {
            "category": category
        })
    else:
        categories = request.POST["category"]
        catechoice = Category.objects.get(name=categories)
        title = request.POST["title"]
        image = request.POST["image"]
        description = request.POST["description"]
        price = request.POST["price"]
        user = request.user
        newItem = Product(
            category = catechoice,
            title = title,
            image = image,
            description = description,
            price = price,
            owner = user
        )
        newItem.save()
        return HttpResponseRedirect(reverse("index"))



def displayItem(request):
    if request.method == "POST":
        selectedCat = request.POST["category"]
        cat = Category.objects.get(name=selectedCat)
        myitems = Product.objects.filter(is_exist = True, category = cat)
        categories = Category.objects.all()
        return render(request, "file/index.html",{
            "items": myitems,
            "category": categories
        })
    
def listing(request, id):
    listingdata = Product.objects.get(pk=id)
    ca = request.user in listingdata.cart.all()
    return render(request, "file/listing.html", {
        "listing": listingdata,
        "cart": ca
    })


def add(request, id):
    listing = Product.objects.get(pk=id)
    user = request.user
    listing.cart.add(user)
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def remove(request, id):
    listing = Product.objects.get(pk=id)
    user = request.user
    listing.cart.remove(user)
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def cart(request):
    cuser = request.user
    listing = cuser.cart.all()
    return render(request, "file/cart.html", {
        "listing": listing
    })



def payment(request, id):
    product = Product.objects.get(pk=id)
    pdid = product.id
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        try:
            charge = stripe.Charge.create(
                amount=product.price,  # Amount in cents ($50.00)
                currency='usd',
                description='Example charge',
                source=token,
            )
            return HttpResponseRedirect(reverse('payment_success'))  # Redirect to a success page
        except stripe.error.StripeError:
            return HttpResponseRedirect(reverse('payment_error')) # Redirect to an error page
    return render(request, 'file/payment.html', {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        'id': pdid,
        'product': product
    })