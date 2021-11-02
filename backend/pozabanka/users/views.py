from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.encoding import force_text, force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from .forms import CustomUserCreationForm
from .models import User


class UserRegistrationView(View):
    form_class = CustomUserCreationForm
    template_name = "users/register.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = "Digital-Desire account activation link"
            message = render_to_string(
                "users/email_template.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": default_token_generator.make_token(user),
                },
            )
            user_email_adress = form.cleaned_data.get("email")
            email = EmailMessage(mail_subject, message, to=[user_email_adress])
            email.send()
            return HttpResponse("Please check your email for activation link")
        return render(request, self.template_name, {"form": form})


class ActivateUserAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return HttpResponse(
                "Thank you for your email confirmation. You are now logged in."
            )
        else:
            return HttpResponse("Activation link is invalid!")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            try:
                user = User.objects.get(email=data)
            except User.DoesNotExist:
                user = None
            if user:
                current_site = get_current_site(request)
                mail_subject = "Digital-Desire password reset"
                message = render_to_string(
                    "users/password_reset_email.html",
                    {
                        "domain": current_site.domain,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                    },
                )
                email = EmailMessage(mail_subject, message, to=[user.email])
                email.send()

                return redirect("password_reset_done")
            return HttpResponse("There is no user with this email.")

    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="users/password_reset.html",
        context={"password_reset_form": password_reset_form},
    )
