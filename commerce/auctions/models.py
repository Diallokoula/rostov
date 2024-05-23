from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.URLField()
    price = models.FloatField()
    is_exist = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    cart = models.ManyToManyField(User, blank=True, null=True, related_name="cart")
    def __str__(self):
        if self.is_exist == True:
            return f"{self.title}: ${self.price} (Available)."
        else:
            return f"{self.title}: Not Available."
