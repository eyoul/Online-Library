from django.shortcuts import render
from . import views

# Create your views here.
def index(request):
    return render(request, 'librarian/base.html', {})

# login and logout .
def logio(request):
    return render(request, 'auth/logio.html', {})

# About Page .
def about(request):
    return render(request, 'about.html', {})

def gchat(request):
    return render(request, 'librarian/group_chat.html', {})

def tbook(request):
    return render(request, 'librarian/add_tbook.html', {})

def rbook(request):
    return render(request, 'librarian/add_rbook.html', {})

