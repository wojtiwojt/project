from django.urls import path
from .views import UserRegistrationView, ActivateUserAccount, password_reset_request
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="registration"),
    path("success/", UserRegistrationView.as_view(), name="success"),
    path("activate/<uidb64>/<token>/", ActivateUserAccount.as_view(), name="activate"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="base.html"), name="logout"),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password_reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/success/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("password_reset", password_reset_request, name="password_reset"),
]
