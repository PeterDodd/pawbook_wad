from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from pawbook.models import Post, Listing, PetPedia, UserProfile
from pawbook.forms import UserProfileForm, UserForm, PostForm, ListingForm

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
    return


def home(request):
    return


def petPedia(request):
    context_dict = {
        "allPosts": PetPedia.objects.all(),
    }


@login_required
def add_post(request):
    return


@login_required
def add_listing(request):
    return


@login_required
def logout(request):
    return


@login_required
def profile(request):
    return