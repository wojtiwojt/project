from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.encoding import force_text, force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .tokens import account_activation_token
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
                    "token": account_activation_token.make_token(user),
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
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return HttpResponse(
                "Thank you for your email confirmation. You are now logged in."
            )
        else:
            return HttpResponse("Activation link is invalid!")
