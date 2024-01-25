from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item


@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    data = {"items": items}

    return render(request, "dashboard/index.html", data)
