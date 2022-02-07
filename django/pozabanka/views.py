from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        user_email = request.user.email
    else:
        user_email = None
    return render(request, "base.html", {"user_email": user_email})
