from home import views
from django.urls import path


# A list of url patterns.
urlpatterns = [
    path("", views.home, name="home"),
    path("contact_us", views.contact_us, name="contact_us"),
]
