from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from PIL import Image


class UserProfile(models.Model):   # User model
    user = models.OneToOneField(User, on_delete = models.CASCADE)   # Link UserProfile to User model instance
    dateJoined = models.DateField(auto_now_add = True)

    firstName = models.CharField(max_length = 32, default = "", blank = True)
    lastName = models.CharField(max_length=32, default="", blank = True)
    bio = models.CharField(max_length = 500, default = "", blank = True)
    location = models.CharField(max_length = 200, default = "", blank = True)

    age = models.IntegerField(default = 0, blank = True)
    sellCount = models.IntegerField(default = 0, blank = True)

    profilePicture = models.ImageField(default = "profile_image/default.jpg", upload_to = "profile_image", blank = True, null = True)
    slug = models.SlugField(unique = True, default = "")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Post(models.Model):           # Image posts model
    poster = models.ForeignKey(UserProfile, on_delete = models.CASCADE)     # Foreign key for user profile
    datePosted = models.DateField(auto_now_add = True)

    postTitle = models.CharField(max_length = 128)
    postDescription = models.CharField(max_length = 300, default = "", blank = True)
    postImage = models.ImageField(upload_to="post_image")

    likes = models.ManyToManyField(User, related_name = 'likes', blank = True)
    dislikes = models.ManyToManyField(User, related_name = "dislikes", blank = True)

    slug = models.SlugField(default = "")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.postTitle)
        super(Post, self).save(*args, **kwargs)


class PetPedia(models.Model):       # Pet-O-Pedia model
    species = models.CharField(max_length=128)
    breed = models.CharField(max_length = 128)
    info = models.CharField(max_length = 128)
    picture = models.ImageField(upload_to="petPedia_image", blank=True, null=True)

    slug = models.SlugField(unique = True, default = "")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.breed)
        super(PetPedia, self).save(*args, **kwargs)


class Listing(models.Model):        # Listing model
    poster = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    requests = models.ManyToManyField(User, related_name="requests", blank = True)

    datePosted = models.DateField(auto_now_add=True)

    breed = models.CharField(max_length = 128)
    petName = models.CharField(max_length = 128)
    description = models.CharField(max_length = 500, default = "", blank = True)
    petAge = models.IntegerField(default = 0)
    petImage = models.ImageField(upload_to="listing_image")
    cost = models.IntegerField(default = 0)

    slug = models.SlugField(unique = True, default = "")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.petName)
        super(Listing, self).save(*args, **kwargs)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comment')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comment')
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique = False, default = "")

    def __str__(self):
        return "{}-{}".format(self.post.postTitle,str(self.user.username))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post.postTitle)
        super(Comment, self).save(*args, **kwargs)

