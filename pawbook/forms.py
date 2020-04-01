from django import forms
from django.contrib.auth.models import User
from pawbook.models import UserProfile, PetPedia, Post, Listing, Contact


class UserForm(forms.ModelForm):        # Form for User objects
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")


class UserProfileForm(forms.ModelForm): # Form for UserProfile objects
    class Meta:
        model = UserProfile
        fields = ("firstName", "lastName", "age", "bio", "location", "profilePicture")


class PostForm(forms.ModelForm):        # Form for new posts
    postTitle = forms.CharField(max_length = 128, help_text = "Enter post title")
    postDescription = forms.CharField(max_length = 128, help_text = "Enter post description")

    likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    dislikes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)

    postImage = forms.ImageField()

    class Meta:
        model = Post
        fields = ("postTitle", "postDescription", "postImage")


class ListingForm(forms.ModelForm):     # Form for new listings
    breed = forms.CharField(max_length = 128, help_text = "Enter the breed of the animal")
    petName = forms.CharField(max_length = 128, help_text = "Enter the name of the pet for sale")
    description = forms.CharField(max_length = 500, help_text = "Enter a description")
    petAge = forms.IntegerField(help_text = "How old is your pet?")

    cost = forms.IntegerField(help_text = "How much does the pet cost?")
    petImage = forms.ImageField()

    class Meta:
        model = Listing
        fields = ("breed", "petName", "description", "petAge", "cost", "petImage")

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name','last_name','email','message')


