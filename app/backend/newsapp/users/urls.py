from django.urls import path
from .views import UserRegistrationView, ActivateUserAccount
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="registration"),
    path("success/", UserRegistrationView.as_view(), name="success"),
    path("activate/<uidb64>/<token>/", ActivateUserAccount.as_view(), name="activate"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="base.html"), name="logout"),
]
