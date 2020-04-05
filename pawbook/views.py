from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages

from pawbook.models import Post, Listing, PetPedia, UserProfile, Comment
from pawbook.forms import UserProfileForm, UserForm, PostForm, ListingForm, ContactForm, CommentForm

from django.contrib.auth import authenticate, login, logout


def home(request):
    queryset_list = Post.objects.all()

    query = request.GET.get("query")
    if query:
        queryset_list = queryset_list.filter(
            Q(postTitle__icontains=query) |
            Q(postDescription__icontains=query) |
            Q(poster__user__username__icontains=query)).distinct()

    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')

    try:
        queryset = paginator.page(page)

    except PageNotAnInteger:
        queryset = paginator.page(1)

    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return render(request, "pawbook/home.html", context = {
        "trendingPosts": Post.objects.order_by("-likes")[:6],
        "latestListings": Listing.objects.order_by("-datePosted")[:6],
        "allPosts": PetPedia.objects.all(),
        "object_list": queryset,
    })


def posts(request):
    form = PostForm()
    queryset_list = Post.objects.all()
    query = request.GET.get("query")

    if query:
        queryset_list = queryset_list.filter(
            Q(postTitle__icontains=query) |
            Q(postDescription__icontains=query) |
            Q(poster__user__username__icontains=query)).distinct()

    paginator = Paginator(queryset_list, 2)
    page = request.GET.get('page')

    try:
        queryset = paginator.page(page)

    except PageNotAnInteger:
        queryset = paginator.page(1)

    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            newPost = Post.objects.create(
                poster = request.user.userprofile,
                postTitle = form.cleaned_data.get("postTitle"),
                postDescription = form.cleaned_data.get("postDescription"),
                postImage = form.cleaned_data.get("postImage")
            )

            newPost.save()

            return redirect("/pawbook/posts/")
        else:
            print(form.errors)
            return redirect("/pawbook/")

    else:
        form = PostForm()

    return render(request, "pawbook/posts.html", context = {
        "newest_posts": Post.objects.order_by("-datePosted"),
        "trending": Post.objects.order_by("-likes")[:6],
        "allPosts": PetPedia.objects.all(),
        "object_list": queryset,
        "postForm": form,
    })


def show_post(request, name_slug):
    context_dict = {}

    try:
        context_dict["post"] = Post.objects.get(slug = name_slug)

    except Post.DoesNotExist:
        context_dict["post"] = None

    try:
        context_dict["comments"] = Comment.objects.filter(slug=name_slug)

    except Comment.DoesNotExist:
        context_dict["comments"] = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)

        if comment_form .is_valid():
            newComment = Comment.objects.create(
                post = Post.objects.get(slug = name_slug),
                user = request.user,
                content = comment_form.cleaned_data.get("content")
            )

            newComment.save()
            return HttpResponseRedirect(request.path_info)

        else:
            print(comment_form.errors)
            return redirect("/pawbook/")

    else:
        comment_form = CommentForm()
        context_dict['comment_form'] = comment_form

    return render(request, "pawbook/postPage.html", context = context_dict)


def like_post(request):
    slug = request.POST.get("post_slug")

    post = get_object_or_404(Post, slug = slug)
    post.likes.add(request.user)

    return show_post(request, slug)


def dislike_post(request):
    slug = request.POST.get("post_slug")

    post = get_object_or_404(Post, slug = slug)
    post.dislikes.add(request.user)

    return show_post(request, slug)


def listings(request):
    form = ListingForm()
    queryset_list = Listing.objects.all()
    query = request.GET.get("query")

    if query:
        queryset_list = queryset_list.filter(
            Q(breed__icontains=query) |
            Q(description__icontains=query) |
            Q(petName__icontains=query) |
            Q(petAge__icontains=query) |
            Q(cost__icontains=query) |
            Q(poster__user__username__icontains=query)).distinct()

    paginator = Paginator(queryset_list, 2)
    page = request.GET.get('page')

    try:
        queryset = paginator.page(page)

    except PageNotAnInteger:
        queryset = paginator.page(1)

    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)

        if form.is_valid():
            newPost = Listing.objects.create(
                poster=request.user.userprofile,
                breed=form.cleaned_data.get("breed"),
                petName=form.cleaned_data.get("petName"),
                description=form.cleaned_data.get("description"),
                petAge = form.cleaned_data.get("petAge"),
                cost = form.cleaned_data.get("cost"),
                petImage = form.cleaned_data.get("petImage")
            )

            newPost.save()
            return redirect("/pawbook/marketplace/")

        else:
            print(form.errors)
            return redirect("/pawbook/")

    else:
        form = ListingForm()

    return render(request, "pawbook/marketplace.html", context = {
        "newest_listings": Listing.objects.all(),
        "allPosts": PetPedia.objects.all(),
        "object_list": queryset,
        "listingForm": form,
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
    queryset_list = PetPedia.objects.all()
    query = request.GET.get("query")

    if query:
        queryset_list = queryset_list.filter(
            Q(species__icontains=query) |
            Q(breed__icontains=query) |
            Q(info__icontains=query)).distinct()

    paginator = Paginator(queryset_list, 2)
    page = request.GET.get('page')

    try:
        queryset = paginator.page(page)

    except PageNotAnInteger:
        queryset = paginator.page(1)

    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return render(request, "pawbook/pet-o-pedia.html", context = {
        "allPosts": PetPedia.objects.all(),
        "object_list": queryset,
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


def userLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")  # Retrieve username
        password = request.POST.get("password")  # and password
        print()
        user = authenticate(username = username, password = password)   # Check all is well with authentication

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse("pawbook:home"))

            else:
                return HttpResponse("Account disabled.")
        else:
            print(user)
            print("Invalid login details: {username}, {password}".format(username=username, password=password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, "pawbook/login.html")


@login_required
def userLogout(request):
    logout(request)
    return redirect(reverse("pawbook:home"))


@login_required
def edit_profile(request, name_slug):
    profile = UserProfile.objects.get(slug = name_slug)

    if request.method == "POST":
        profile_form = UserProfileForm(request.POST, initial = {
            "firstName":    profile.firstName,
            "lastName":     profile.lastName,
            "age":          profile.age,
            "bio":          profile.bio,
            "location":     profile.location,
        }, instance = profile)

        if profile_form.is_valid():
            # profile = profile_form.save(commit=False)

            if "profilePicture" in request.FILES:
                profile.profilePicture = request.FILES["profilePicture"]

            profile.user = request.user
            profile.save()

            return HttpResponseRedirect(reverse('pawbook:show_profile', kwargs={"name_slug": name_slug}))

        else:
            print(profile_form.errors)

    else:
        profile_form = UserProfileForm(initial = {
            "firstName":    profile.firstName,
            "lastName":     profile.lastName,
            "age":          profile.age,
            "bio":          profile.bio,
            "location":     profile.location,
        }, instance = profile)

    return render(request, "pawbook/editProfile.html", context={
        "profileForm": profile_form
    })


def show_profile(request, name_slug):
    return render(request, "pawbook/userProfile.html", context = {
        "userProfile": UserProfile.objects.get(slug = name_slug)
    })


def about(request):
    return render(request, "pawbook/about.html")


def faq(request):
    return render(request, "pawbook/faq.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Form submission successful")

    else:
        form = ContactForm()

    return render(request, "pawbook/contact.html", {'form':form})

