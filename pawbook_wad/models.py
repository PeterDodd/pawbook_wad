from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):   #User model
    #Link UserProfile to User model instance
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    age = models.IntegerField()
    bio = models.CharField()
    sellCount = models.IntegerField(default = 0)
    location = models.CharField()
    profilePicture = ImageField(upload_to = "profile_image", blank = true)

    def __str__(self):
        return self.user.username


class Post(model.Models):           #Image posts model
    poster = models.ForeignKey(UserProfile, on_delete = models.CASCADE) #Foreign key for user profile
    postTitle = models.CharField(max_length = 128)
    #datePosted
    postImage = models.ImageField(upload_to = "post_image")
    postDescription = models.CharField(max_length = 300)
    Likes = models.IntegerField(default = 0)
    Dislikes = models.IntegerField(default = 0)


class Listing(model.Models):        #Listing model
    poster = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    breed = models.ForeignKey(PetPedia, on_delete = models.CASCADE)
    #datePosted
    petName = models.CharField(max_length = 128)
    petAge = models.IntegerField()
    cost = models.IntegerField()
    petImage = models.ImageField(upload_to = "listing_image")


class PetPedia(model.Models):       #Pet-O-Pedia model
    breed = models.CharField(max_length = 128)
    species = models.CharField(max_length = 128)
    info = models.CharField(max_length = 128)
    picture = models.ImageField(upload_to = "petPedia_image")
