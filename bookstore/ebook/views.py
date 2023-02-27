from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages


from . import views 
# from . forms import SignUpForm
# from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# login and logout .
def home(request):
    return render(request, 'dashboard/home.html', {})

# User is authenticated
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_admin or user.is_superuser:
                return redirect('dashboard')
            elif user.is_librarian:
                return redirect('librarian')
            elif user.is_publisher:
                return redirect('publisher')
            else:
                return redirect('student')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('home')




