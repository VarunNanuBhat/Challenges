from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name= "home_page"),
    path("<month>/", views.monthly_challenge, name = "monthly_challenge"),
]
