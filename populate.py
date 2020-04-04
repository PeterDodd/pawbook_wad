# Populates the database for testing
import django
import os
import random

from django.core.files import File
from django.core.files.images import ImageFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pawbook_wad.settings')
django.setup()

from pawbook.models import Post, Listing, UserProfile, PetPedia
from django.contrib.auth.models import User
from django.conf import settings

def populate():
    testUsers = [
        ("John123", "John", "Smith", "I'm interested in LOLcats and stuff", "London"),
        ("Adam69", "Adam", "", "I sell puppies for decent prices hmu", ""),
        ("coolkid1337", "", "", "Exotic pet trafficker", "")
    ]

    testPosts = [
        ("My first post", "Here are some pictures of my cats", "CatPost.png"),
        ("Looking after fish", "Incredibly relevant question about caring for fish", "fishPost.jpg"),
        ("Looking to sell [Is this the right section?]", "Looking to sell my cat", "catSale.jpg"),
        ("Subscribe to my insta", "I post cat videos on it", "insta.jpeg"),
        ("Find us on facebook", "Search for us", "facebook.png"),
        ("Find us on Twitter", "Search for us", "twitter.png"),
        ("Find us on BeBo", "Search for us", "bebo.jpg"),
        ("First post", "This is a test post", "pufferFish.jpeg")
    ]

    testListings = [
        ("Fluffs", "We are moving so we need to find her a new home", "Cat", "cat.jpg"),
        ("N/A", "Looking to sell lab puppies locally", "Dog", "lab.jpg"),
        ("ExoticFish", "Selling fish", "Fish", "fish.jpeg")
    ]

    testPets = [
        ("Dog", "Lab", "There are lots of different types of dogs", "lab.jpg"),
        ("Cow", "Some breed of cow", "There are a few types of cow, this is where we get our milk", "cow.jpg"),
        ("Cat", "Tabby", "Cats are made of yoghurt inside", "cat.jpg")
    ]

    userList = [add_user(user[0], user[1], user[2], user[3], user[4])
                for user in testUsers]

    petPages = [add_pet(pet[0], pet[1], pet[2], pet[3])
                for pet in testPets]

    listings = [add_listing(userList, listing[2], listing[0], listing[1], listing[3])
                for listing in testListings]

    posts = [add_post(userList, post[0], post[1], post[2])
             for post in testPosts]


def add_user(username, firstName, lastName, bio, location):
    print("Username: " + username)
    newUser = User.objects.get_or_create(
        username = username,
        password = "Test",
        email = "test@test.com"
    )[0]
    newUser.set_password(newUser.password)
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


def add_pet(species, breed, info, image):
    newPage = PetPedia.objects.get_or_create(
        species = species,
        breed = breed,
        info = info
    )[0]

    newPage.picture.save(image, ImageFile(open(settings.MEDIA_ROOT + "/petPedia_image/" + image, 'rb')))

    return newPage


def add_post(allUsers, title, description, image):
    newPost = Post.objects.get_or_create(
        poster = random.choice(allUsers),
        postTitle = title,
        postDescription = description,
    )[0]

    newPost.postImage.save(image, ImageFile(open(settings.MEDIA_ROOT + "/post_image/" + image, 'rb')))

    return newPost


def add_listing(allUsers, breed, name, description, image):
    newListing = Listing.objects.get_or_create(
        poster = random.choice(allUsers),
        breed = breed,
        petName = name,
        description = description,
        petAge = random.randint(0, 10),
        cost = random.randint(0, 150),
    )[0]

    newListing.petImage.save(image, ImageFile(open(settings.MEDIA_ROOT + "/listing_image/" + image, 'rb')))

    return newListing

if __name__ == '__main__':
    print('Starting population script...')
    populate()
