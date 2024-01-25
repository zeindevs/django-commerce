from django.shortcuts import render

from item.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    data = {"categories": categories, "items": items}

    return render(request, "core/index.html", data)


def contact(request):
    return render(request, "core/contact.html")
