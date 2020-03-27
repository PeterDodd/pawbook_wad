from django.urls import path

from pawbook import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "pawbook"

urlpatterns = [
    path('', views.home, name='home'),

    path('marketplace/', views.listings, name='marketplace'),
    path("marketplace/<slug:name_slug>/", views.show_listing, name = "show_listing"),

    path('posts/', views.posts, name='posts'),
    path("posts/<slug:name_slug>/", views.show_post, name = "show_post"),

    path('pet-o-pedia/', views.pet_pedia, name='pet-o-pedia'),
    path("pet-o-pedia/<slug:name_slug>/", views.show_petPedia, name = "show_petPedia"),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

