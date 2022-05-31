from django.urls import path
from . import views

# A list of url patterns.
urlpatterns = [
    path("", views.youtube_view, name="youtube"),
]
