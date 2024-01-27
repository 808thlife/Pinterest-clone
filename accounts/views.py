from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .models import User

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("core:index"))
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        print(user)
        print(User.objects.get(email = email))
        # Check if authentication successful
        if user is not None:
            
            login(request, user)
            return HttpResponseRedirect(reverse("core:index"))
        else:
            return render(request, "accounts/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "accounts/login.html")
    return render(request, "accounts/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "accounts/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "accounts/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("core:index"))
    else:
        return render(request, "accounts/register.html")
    return render(request, "accounts/register.html")

def logout(request):
    pass