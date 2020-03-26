from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from pawbook.models import Post, Listing, PetPedia, UserProfile
from pawbook.forms import UserProfileForm, UserForm, PostForm, ListingForm

from django.contrib.auth import authenticate, login, logout


def posts(request):
    context_dict = {
        "newest_posts": Post.objects.all(),
        "allPosts":     PetPedia.objects.all(),
    }

    return render(request, "pawbook/posts.html", context = context_dict)


def show_post(request, name_slug):
    context_dict = {}

    try:
        post = Post.objects.get(slug = name_slug)
        context_dict["post"] = post

    except Post.DoesNotExist:
        context_dict["post"] = None

    return render(request, "pawbook/postPage.html", context = context_dict)


def listings(request):
    context_dict = {
        "newest_listings": Listing.objects.all(),
        "allPosts":        PetPedia.objects.all(),
    }

    return render(request, "pawbook/marketplace.html", context = context_dict)


def show_listing(request, name_slug):
    context_dict = {}

    try:
        listing = Listing.objects.get(slug = name_slug)
        context_dict["listing"] = listing

    except Listing.DoesNotExist:
        context_dict["listing"] = None

    return render(request, "pawbook/listingPage.html", context = context_dict)


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
            print("Invalid login details: {username}, {password}")

    else:
        return render(request, "pawbook/login.html")


def home(request):
    context_dict = {
        "trendingPosts":    Post.objects.order_by("-likes")[:6],
        "latestListings":   Listing.objects.order_by("-datePosted")[:6],
        "allPosts":         PetPedia.objects.all(),
    }

    return render(request, "pawbook/home.html", context = context_dict)


def pet_pedia(request):
    context_dict = {
        "allPosts": PetPedia.objects.all(),
    }

    return render(request, "pawbook/pet-o-pedia.html", context = context_dict)


def show_petPedia(request, name_slug):
    context_dict = {
        "allPosts": PetPedia.objects.all(),
    }

    try:
        page = PetPedia.objects.get(slug = name_slug)
        context_dict["page"] = page

    except PetPedia.DoesNotExist:
        context_dict["page"] = None

    return render(request, "pawbook/petPediaPage.html", context = context_dict)


def about(request):

    return render(request, "pawbook/about.html")


def faq(request):

    return render(request, "pawbook/faq.html")


def contact(request):

    return render(request, "pawbook/contact.html", context = {"allPosts": PetPedia.objects.all()})


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

        else:
            print(form.errors)

    return render(request, "pawbook/add_listing.html", {"form": form})


@login_required
def logout(request):
    logout(request)
    return redirect(reverse("pawbook:home"))


@login_required
def profile(request):
    return

