from django.contrib import admin

# Register your models here.
from django.contrib import admin
from pawbook.models import UserProfile, Post, PetPedia, Listing, Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ("postTitle", "poster", "datePosted")


class PetPediaAdmin(admin.ModelAdmin):
    list_display = ("species", "breed")


class ListingAdmin(admin.ModelAdmin):
    list_display = ("poster", "petName", "breed", "cost")


admin.site.register(UserProfile)
admin.site.register(Post, PostAdmin)
admin.site.register(PetPedia, PetPediaAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Contact)