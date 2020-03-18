from django.urls import path
from pawbook import views

app_name = "pawbook"

urlpatterns = [
    path('', views.home, name='home'),
    path('marketplace/', views.listings, name='marketplace'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('posts/', views.posts, name='posts'),
    path('pet-o-pedia/', views.pet_pedia, name='pet-o-pedia'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]