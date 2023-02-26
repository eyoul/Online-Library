from django.shortcuts import render
from . import views

# Create your views here.
def index(request):
    return render(request, 'publisher/base.html', {})

# login and logout .
def logio(request):
    return render(request, 'auth/logio.html', {})

# About Page .
def about(request):
    return render(request, 'about.html', {})



