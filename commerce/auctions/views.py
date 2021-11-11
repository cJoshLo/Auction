from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# from django.forms import ModelFrom, modelfromset_factory
from django.forms import ModelForm
from django.contrib import messages

from .models import Items, Bid, Comments, User
from .forms import BidForm, CommentForm, ListingForm




def index(request):
    return render(request, "auctions/index.html",{
        "items" : Items.objects.all()
    })

@login_required()  
def add(request):
    form = ListingForm()

    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            section = form.save(commit=False)
            section.creator = request.user
            section.currentBider = request.user
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            form = ListingForm()

    context = {'form':form}
    return render(request, "auctions/add.html", context)

@login_required()    
def items(request, Items_id):
    form3 = BidForm()
    items_full = Items.objects.get(pk=Items_id)
    if request.method == "POST":
        form3 = BidForm(request.POST, request.FILES)
        if form3.is_valid():
            section = form3.save(commit=False)
            if section.offer > items_full.startingBid:
                Items.objects.filter(pk=Items_id).update(startingBid=section.offer)
                Items.objects.filter(pk=Items_id).update(currentBider=request.user)

            section.auction = items_full

            form3.save()
            return HttpResponseRedirect(reverse("item_page", args=[Items_id]))
        else:
            form3 = BidForm()

    items = Items.objects.get(pk=Items_id)
    comment_list = Comments.objects.all().filter(item_reference_id = Items_id)
    return render(request, "auctions/item.html",{
        "items_full" : items_full,
        "items": items,
        "comments" : comment_list,
        'form': form3,
    })

def delete(request, Items_id):
    items_full = Items.objects.get(pk=Items_id)
    items_full.delete()
    return render(request, "auctions/index.html",{
        "items" : Items.objects.all()
    })



@login_required()  
def comment(request, Items_id):
    form2 = CommentForm()
    items_full = Items.objects.get(pk=Items_id)
    if request.method == "POST":
        form2 = CommentForm(request.POST, request.FILES)
        if form2.is_valid():
            section = form2.save(commit=False)
            section.user = request.user
            section.item_reference = items_full
            form2.save()
            return HttpResponseRedirect(reverse("item_page", args=[Items_id]))
        else:
            form2 = CommentForm()

    items = Items.objects.get(pk=Items_id)
    return render(request, "auctions/comment.html",{
        "items_full" : items_full,
        "items": items,
        'form': form2,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
