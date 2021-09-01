from django.conf import settings
from django.urls import include, path, re_path



urlpatterns = [
    path("api/", include("core.urls.api")),
    ]