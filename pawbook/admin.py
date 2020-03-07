from django.contrib import admin
from pawbook.models import UserProfile, Post, PetPedia, Listing


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "dateJoined")


class PostAdmin(admin.ModelAdmin):
    list_display = ("postTitle", "poster", "datePosted")


class PetPediaAdmin(admin.ModelAdmin):
    list_display = ("breed", "species")


class ListingAdmin(admin.ModelAdmin):
    list_display = ("poster", "petName", "breed", "datePosted")


admin.site.register(UserProfile, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PetPedia, PetPediaAdmin)
admin.site.register(Listing, ListingAdmin)
