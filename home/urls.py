from django.urls import path
from . import views
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# A list of url patterns.
urlpatterns = [
    path("", views.home, name="home"),
    path("contact_us", views.contact_us, name="contact_us")
]

handler404 = "home.views.error_404_view"

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)