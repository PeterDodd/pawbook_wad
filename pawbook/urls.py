from django.urls import path
from pawbook import views

app_name = "pawbook"

urlpatterns = [
    path('', views.home, name='home'),
]