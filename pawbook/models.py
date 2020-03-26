from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UserProfile(models.Model):   # User model
    user = models.OneToOneField(User, on_delete = models.CASCADE)   # Link UserProfile to User model instance
    dateJoined = models.DateField(auto_now_add = True)

    firstName = models.CharField(max_length = 32, default = "", blank = True)
    lastName = models.CharField(max_length=32, default="", blank = True)
    bio = models.CharField(max_length = 500, default = "", blank = True)
    location = models.CharField(max_length = 200, default = "", blank = True)

    age = models.IntegerField(default = 0, blank = True)
    sellCount = models.IntegerField(default = 0, blank = True)

    profilePicture = models.ImageField(upload_to = "profile_image", default = None, blank = True)

    def __str__(self):
        return self.user.username


class Post(models.Model):           # Image posts model
    poster = models.ForeignKey(UserProfile, on_delete = models.CASCADE)     # Foreign key for user profile
    datePosted = models.DateField(auto_now_add = True)

    postTitle = models.CharField(max_length = 128)
    postDescription = models.CharField(max_length = 300, default = "", blank = True)

    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)

    slug = models.SlugField(unique = True, default = "")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.postTitle)
        super(Post, self).save(*args, **kwargs)

    postImage = models.ImageField(upload_to = "post_image", default = None, blank = True)


class PetPedia(models.Model):       # Pet-O-Pedia model
    species = models.CharField(max_length=128)
    breed = models.CharField(max_length = 128)
    info = models.CharField(max_length = 128)

    slug = models.SlugField(unique = True, default = "")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.breed)
        super(PetPedia, self).save(*args, **kwargs)

    picture = models.ImageField(upload_to = "petPedia_image", default = None, blank = True)


class Listing(models.Model):        # Listing model
    poster = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    datePosted = models.DateField(auto_now_add=True)

    breed = models.CharField(max_length = 128)
    petName = models.CharField(max_length = 128)
    description = models.CharField(max_length = 500, default = "", blank = True)
    petAge = models.IntegerField(default = 0)

    cost = models.IntegerField(default = 0)

    slug = models.SlugField(unique = True, default = "")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.petName)
        super(Listing, self).save(*args, **kwargs)

    petImage = models.ImageField(upload_to = "listing_image", default = None, blank = True)
