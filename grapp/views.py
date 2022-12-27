from django.shortcuts import render

# Create your views here.
from .models import user


def home(request):
    name = user.objects.all()
    return render(request, "grapp/home.html", {"name": name})
