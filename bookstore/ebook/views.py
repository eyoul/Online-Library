from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'dashboard/base.html', {})

# login and logout .
def logio(request):
    return render(request, 'auth/logio.html', {})

# About Page .
def about(request):
    return render(request, 'about.html', {})

def gchat(request):
    return render(request, 'group_chat.html', {})