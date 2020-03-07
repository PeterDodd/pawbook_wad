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
