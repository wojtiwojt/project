from django.urls import include, path

urlpatterns = [
    path("v1/", include("core.urls.v1")),
]
