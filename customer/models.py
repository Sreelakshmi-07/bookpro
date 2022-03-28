from django.db import models
from book_form.models import Books
from django.contrib.auth.models import User


# django.contrib.outh
# Create your models here.
class Carts(models.Model):
    product = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    # qty = models.PositiveIntegerField(default=1)
    # in cart,orderplaced,cancelled
    options = (
        ("incart","incart"),
        ("orderplaced","orderplaced"),
        ("cancelled","cancelled")
    )
    status = models.CharField(max_length=20,choices=options,default="incart")

#
# class User(models.Model):
#     first_name=models.CharField(max_length=120)
#     last_name=models.CharField(max_length=120)
#     email = models.CharField(max_length=120,unique=True)
#     username = models.CharField(max_length=120,unique=True)
