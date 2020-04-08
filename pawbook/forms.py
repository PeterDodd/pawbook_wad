from django import forms
from django.contrib.auth.models import User
from pawbook.models import UserProfile, PetPedia, Post, Listing, Contact, Comment


class UserForm(forms.ModelForm):        # Form for User objects
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")
        widgets = {
            "username": forms.TextInput(attrs={'placeholder': 'USERNAME', 'id': 'top'}),
            "email": forms.TextInput(attrs={'placeholder': 'EMAIL'}),
            "password": forms.TextInput(attrs={'placeholder': 'PASSWORD'})}


class UserProfileForm(forms.ModelForm): # Form for UserProfile objects
    class Meta:
        model = UserProfile
        fields = ("firstName", "lastName", "age", "bio", "location", "profilePicture")
        widgets = {
            "firstName": forms.TextInput(attrs={'placeholder': 'FIRST NAME', 'id': 'top'}),
            "lastName": forms.TextInput(attrs={'placeholder': 'LAST NAME'}),
            "age": forms.NumberInput(attrs={'placeholder': 'AGE'}),
            "bio": forms.TextInput(attrs={'placeholder': 'BIO'}),
            "location": forms.TextInput(attrs={'placeholder': 'LOCATION'})}


class PostForm(forms.ModelForm):        # Form for new posts
    postTitle = forms.CharField(max_length = 128, widget=forms.TextInput(attrs={'placeholder': 'TITLE', 'id': 'top'}))
    postDescription = forms.CharField(max_length = 128, widget=forms.TextInput(attrs={'placeholder': 'DESCRIPTION'}))

    likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    dislikes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)

    slug = forms.CharField(widget = forms.HiddenInput(), required = False)
    postImage = forms.ImageField()

    class Meta:
        model = Post
        fields = ("postTitle", "postDescription", "postImage")


class ListingForm(forms.ModelForm):     # Form for new listings
    breed = forms.CharField(max_length = 128, widget=forms.TextInput(attrs={'placeholder': 'BREED', 'id': 'top'}))
    petName = forms.CharField(max_length = 128, widget=forms.TextInput(attrs={'placeholder': 'PET NAME'}))
    description = forms.CharField(max_length = 500, widget=forms.TextInput(attrs={'placeholder': 'DESCRIPTION'}))
    petAge = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'PET AGE'}))

    cost = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'PRICE'}))
    petImage = forms.ImageField()

    class Meta:
        model = Listing
        fields = ("breed", "petName", "description", "petAge", "cost", "petImage")


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name','last_name','email','message')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'content',}

