# Populates the database for testing
import django
import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pawbook_wad.settings')
django.setup()

from pawbook.models import Post, Listing, UserProfile, PetPedia
from django.contrib.auth.models import User


def populate():
    testUsers = [
        ("John", "I'm interested in LOLcats and stuff"),
        ("Adam69", "I sell puppies for decent prices hmu"),
        ("coolkid1337", "Exotic pet trafficker")
    ]

    testPosts = [
        ("My first post", "Here are some pictures of my cats"),
        ("Looking after fish", "Incredibly relevant question about caring for fish"),
        ("Looking to sell [Is this the right section?]", "Looking to sell my cat"),
        ("Subscribe to my insta", "I post cat videos on it"),
        ("Find us on facebook", "Search for us"),
        ("Find us on Twitter", "Search for us"),
        ("Find us on BeBo", "Search for us"),
        ("First post", "This is a test post")
    ]

    testListings = [
        ("Fluffs", "We are moving so we need to find her a new home"),
        ("N/A", "Looking to sell lab puppies locally"),
        ("ExoticFish", "Selling fish")
    ]

    testPets = [
        ("Dog", "Lab", "There are lots of different types of dogs"),
        ("Cow", "Some breed of cow", "There are a few types of cow, this is where we get our milk"),
        ("Cat", "Tabby", "Cats are made of yoghurt inside")
    ]

    userList = [add_user(user[0], user[1])
                for user in testUsers]

    petPages = [add_pet(pet[0], pet[1], pet[2])
                for pet in testPets]

    listings = [add_listing(userList, petPages, listing[0], listing[1])
                for listing in testListings]

    posts = [add_post(userList, post[0], post[1])
             for post in testPosts]


def add_user(username, bio):
    newUser = User.objects.get_or_create(
        username = username,
        password = "Test",
        email = "test@test.com"
    )[0]

    newUserProfile = UserProfile.objects.get_or_create(
        user = newUser,
        username = newUser.username,
        bio = bio,
        sellCount = random.randint(0, 50)
    )[0]

    newUser.save()
    newUserProfile.save()

    return newUser


def add_pet(species, breed, info):
    newPage = PetPedia.objects.get_or_create(
        species = species,
        breed = breed,
        info = info
    )[0]

    newPage.save()

    return newPage


def add_post(allUsers, title, description):
    newPost = Post.objects.get_or_create(
        poster = random.choice(allUsers),
        postTitle = title,
        postDescription = description,
        likes = random.randint(0, 1000),
        dislikes = random.randint(0, 1000)
    )[0]

    newPost.save()

    return newPost


def add_listing(allUsers, allBreeds, name, description):
    newListing = Listing.objects.get_or_create(
        poster = random.choice(allUsers),
        breed = random.choice(allBreeds),
        petName = name,
        description = description,
        petAge = random.randint(0, 10),
        cost = random.randint(0, 150)
    )[0]

    newListing.save()

    return newListing


populate()
