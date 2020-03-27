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
        ("John123", "John", "Smith", "I'm interested in LOLcats and stuff", "London"),
        ("Adam69", "Adam", "", "I sell puppies for decent prices hmu", ""),
        ("coolkid1337", "", "", "Exotic pet trafficker", "")
    ]

    testPosts = [
        ("My first post", "Here are some pictures of my cats", "media/post_image/CatPost.png"),
        ("Looking after fish", "Incredibly relevant question about caring for fish", "media/post_image/fishPost.jpg"),
        ("Looking to sell [Is this the right section?]", "Looking to sell my cat", "media/post_image/catSale.jpg"),
        ("Subscribe to my insta", "I post cat videos on it", "media/post_image/insta.jpeg"),
        ("Find us on facebook", "Search for us", "media/post_image/facebook.png"),
        ("Find us on Twitter", "Search for us", "media/post_image/twitter.png"),
        ("Find us on BeBo", "Search for us", "media/post_image/bebo.jpg"),
        ("First post", "This is a test post", "media/post_image/pufferFish.jpeg")
    ]

    testListings = [
        ("Fluffs", "We are moving so we need to find her a new home", "Cat", "media/listing_image/cat.jpg"),
        ("N/A", "Looking to sell lab puppies locally", "Dog", "media/listing_image/lab.jpg"),
        ("ExoticFish", "Selling fish", "Fish", "media/listing_image/fish.jpeg")
    ]

    testPets = [
        ("Dog", "Lab", "There are lots of different types of dogs"),
        ("Cow", "Some breed of cow", "There are a few types of cow, this is where we get our milk"),
        ("Cat", "Tabby", "Cats are made of yoghurt inside")
    ]

    userList = [add_user(user[0], user[1], user[2], user[3], user[4])
                for user in testUsers]

    petPages = [add_pet(pet[0], pet[1], pet[2])
                for pet in testPets]

    listings = [add_listing(userList, listing[2], listing[0], listing[1], listing[3])
                for listing in testListings]

    posts = [add_post(userList, post[0], post[1], post[2])
             for post in testPosts]


def add_user(username, firstName, lastName, bio, location):
    newUser = User.objects.get_or_create(
        username = username,
        password = "Test",
        email = "test@test.com"
    )[0]

    newUser.save()

    newUserProfile = UserProfile.objects.get_or_create(
        user = newUser,
        firstName = firstName,
        lastName = lastName,
        bio = bio,
        location = location,
        age = random.randint(0, 80),
        sellCount = random.randint(0, 50)
    )[0]

    newUserProfile.save()

    return newUserProfile


def add_pet(species, breed, info):
    newPage = PetPedia.objects.get_or_create(
        species = species,
        breed = breed,
        info = info
    )[0]

    newPage.save()

    return newPage


def add_post(allUsers, title, description, image):
    newPost = Post.objects.get_or_create(
        poster = random.choice(allUsers),
        postTitle = title,
        postDescription = description,
        likes = random.randint(0, 1000),
        dislikes = random.randint(0, 1000),
        postImage = image
    )[0]

    newPost.save()

    return newPost


def add_listing(allUsers, breed, name, description, image):
    newListing = Listing.objects.get_or_create(
        poster = random.choice(allUsers),
        breed = breed,
        petName = name,
        description = description,
        petAge = random.randint(0, 10),
        cost = random.randint(0, 150),
        petImage = image
    )[0]

    newListing.save()

    return newListing


populate()
