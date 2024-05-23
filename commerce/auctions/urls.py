from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createProduct", views.createProduct, name="createProduct"),
    path("displayItem", views.displayItem, name="displayItem"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("cart", views.cart, name="cart"),
    path("add/<int:id>", views.add, name="add"),
    path("remove/<int:id>", views.remove, name="remove"),
    path("payment/<int:id>", views.payment, name="payment")
]

