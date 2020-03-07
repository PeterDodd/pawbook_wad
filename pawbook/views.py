from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from pawbook.models import Post, Listing, PetPedia, UserProfile
from pawbook.forms import UserProfileForm, UserForm, PostForm, ListingForm

from django.contrib.auth import authenticate, login, logout


def posts(request):
    context_dict = {
        "newest_posts": Post.objects.order_by("datePosted"),
    }

    return render(request, "pawbook/posts.html", context = context_dict)


def listings(request):
    context_dict = {
        "newest_listings": Listing.objects.order_by("datePosted"),
    }

    return render(request, "pawbook/marketplace.html", context = context_dict)


def register(request):
    registered = False

    if request.method == "POST":
        # Get raw form info
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        # Check forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if "profilePicture" in request.FILES:
                profile.profilePicture = request.FILES["profilePicture"]

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm

    context_dict = {
        "userForm": user_form,
        "profileForm": profile_form
    }

    return render(request, "pawbook/register.html", context = context_dict)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")  # Retrieve username
        password = request.POST.get("password")  # and password

        user = authenticate(username = username, password = password)   # Check all is well with authentication

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse("pawbook:home"))

            else:
                return HttpResponse("Account disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")

    else:
        return render(request, "pawbook/login.html")


def home(request):
    context_dict = {
        "trendingPosts":    Post.objects.order_by("-likes")[:6],
        "latestListings":   Listing.objects.order_by("-datePosted")[:6]
    }

    return render(request, "pawbook/home.html", context = context_dict)


def petPedia(request):
    context_dict = {
        "allPosts": PetPedia.objects.all(),
    }


@login_required
def add_post(request):
    postForm = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save(commit = True)

            return redirect("/pawbook/")

        else:
            print(form.errors)


@login_required
def add_listing(request):
    listingForm = ListingForm()

    if request.method == "POST":
        form = ListingForm(request.POST)

        if form.is_valid():
            form.save(commit = True)

            return redirect("/pawbook/")

    return


@login_required
def logout(request):
    logout(request)
    return redirect(reverse("pawbook:home"))


@login_required
def profile(request):
    return