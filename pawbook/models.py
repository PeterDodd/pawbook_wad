from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):   # User model
    user = models.OneToOneField(User, on_delete = models.CASCADE)   # Link UserProfile to User model instance

    dateJoined = models.DateField(default = datetime.now())
    age = models.IntegerField()
    bio = models.CharField()
    location = models.CharField()
    sellCount = models.IntegerField(default=0)
    profilePicture = models.ImageField(upload_to = "profile_image", blank = True)

    def __str__(self):
        return self.user.username


class Post(models.Model):           # Image posts model
    poster = models.ForeignKey(UserProfile, on_delete = models.CASCADE)     # Foreign key for user profile
    postTitle = models.CharField(max_length = 128)
    datePosted = models.DateField(default = datetime.now())
    postImage = models.ImageField(upload_to = "post_image")
    postDescription = models.CharField(max_length = 300)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)


class PetPedia(models.Model):       # Pet-O-Pedia model
    breed = models.CharField(max_length = 128)
    species = models.CharField(max_length = 128)
    info = models.CharField(max_length = 128)
    picture = models.ImageField(upload_to = "petPedia_image")


class Listing(models.Model):        # Listing model
    poster = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    breed = models.ForeignKey(PetPedia, on_delete = models.CASCADE)
    datePosted = models.DateField(default = datetime.now())
    petName = models.CharField(max_length = 128)
    petAge = models.IntegerField()
    cost = models.IntegerField()
    petImage = models.ImageField(upload_to = "listing_image")



