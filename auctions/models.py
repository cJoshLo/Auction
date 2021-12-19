from django.contrib.auth.models import AbstractUser

from django.utils import timezone

from django.db import models
from django.db.models import Model
from django.apps import AppConfig
from django.db.models.fields.related import OneToOneField


class User(AbstractUser):
    pass
    def __str__(self):
        return f"{self.username}"

class Items(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField(max_length = 250)
    created_date = models.DateTimeField(default = timezone.now)
    image = models.ImageField(null=True, blank=True)
    startingBid = models.PositiveIntegerField(blank=False, default=0)
    currentBider = models.ForeignKey(User,null=True, on_delete=models.PROTECT, related_name="top_bider")
    # active = models.BooleanField(default=True)
    creator = models.ForeignKey(User,null=True, on_delete=models.PROTECT, related_name="all_creator_listings")
    # watchers = models.ManyToManyField(User, blank = True, related_name="watched_listings")
    buyer = models.ForeignKey(User,null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title} : {self.startingBid}"

class Bid(models.Model):
    auction = models.ForeignKey(Items, on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    offer = models.FloatField(null=False, default=0)
    # date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.offer}"

class Comments(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length= 200)
    createdDate = models.DateTimeField(default=timezone.now)
    item_reference = models.ForeignKey(Items, null=True, on_delete=models.CASCADE, related_name="get_comment")

    def __str__(self):
        return f"{self.comment} "
