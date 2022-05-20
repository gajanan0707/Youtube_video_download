from django.urls import path
from . import views

# A list of url patterns.
urlpatterns = [
    path("", views.home, name="home"),
    path("contact_us", views.contact_us, name="contact_us")
]
