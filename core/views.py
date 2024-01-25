from django.contrib.auth import logout
from django.shortcuts import redirect, render

from core.forms import SignupForm
from item.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    data = {"categories": categories, "items": items}

    return render(request, "core/index.html", data)


def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/login/")
    else:
        form = SignupForm()

    data = {"form": form}

    return render(request, "core/signup.html", data)


def auth_logout(request):
    logout(request)
    return redirect("/login/")
