from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from pawbook.models import Post, Listing, PetPedia, UserProfile
from pawbook.forms import UserProfileForm, UserForm, PostForm, ListingForm

from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "pawbook/home.html", context = {
        "trendingPosts": Post.objects.order_by("-likes")[:6],
        "latestListings": Listing.objects.order_by("-datePosted")[:6],
        "allPosts": PetPedia.objects.all(),
    })


def posts(request):
    return render(request, "pawbook/posts.html", context = {
        "newest_posts": Post.objects.order_by("-datePosted"),
        "trending": Post.objects.order_by("-likes")[:6],
        "allPosts": PetPedia.objects.all(),
    })


def show_post(request, name_slug):
    context_dict = {}
    try:
        post = Post.objects.get(slug = name_slug)
        context_dict["post"] = post

    except Post.DoesNotExist:
        context_dict["post"] = None

    return render(request, "pawbook/postPage.html", context = context_dict)


def listings(request):
    return render(request, "pawbook/marketplace.html", context = {
        "newest_listings": Listing.objects.all(),
        "allPosts": PetPedia.objects.all(),
    })


def show_listing(request, name_slug):
    context_dict = {}
    try:
        listing = Listing.objects.get(slug = name_slug)
        context_dict["listing"] = listing

    except Listing.DoesNotExist:
        context_dict["listing"] = None

    return render(request, "pawbook/listingPage.html", context = context_dict)


def pet_pedia(request):
    return render(request, "pawbook/pet-o-pedia.html", context = {
        "allPosts": PetPedia.objects.all(),
    })


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

            p = profile_form.save(commit = False)
            p.user = user

            if "picture" in request.FILES:
                p.picture = request.FILES["picture"]

            p.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, "pawbook/register.html", context = {
        "userForm": user_form,
        "profileForm": profile_form,
        "registered": registered
    })


@login_required
def show_profile(request):
    return render(request, "pawbook/userProfile.html", context = {
        "user": request.user,
        "userProfile": UserProfile.objects.filter(user = request.user)
    })


@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = UserProfileForm(request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)

            if "profilePicture" in request.FILES:
                profile.profilePicture = request.FILES["profilePicture"]

            profile.save()

        else:
            print(profile_form.errors)

    else:
        profile_form = UserProfileForm

    return render(request, "pawbook/editProfile.html", context={
        "profileForm": profile_form
    })


def userLogin(request):
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
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, "pawbook/login.html")


def about(request):
    return render(request, "pawbook/about.html")


def faq(request):
    return render(request, "pawbook/faq.html")


def contact(request):
    return render(request, "pawbook/contact.html", context = {
        "allPosts": PetPedia.objects.all()
    })


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
def userLogout(request):
    logout(request)
    return redirect(reverse("pawbook:home"))


@login_required
def profile(request):
    return

