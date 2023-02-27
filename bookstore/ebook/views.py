from django.shortcuts import render
from . import views 
# from . forms import SignUpForm
# from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# # login and logout .
# def logio(request):
#     return render(request, 'auth/logio.html', {})

# # About Page .
# def about(request):
#     return render(request, 'about.html', {})


# def register_form(request):
#     if request.method == 'POST':
#         forms = SignUpForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return HttpResponseRedirect('index.html')
#     return render(request, 'auth/rigist.html', {})




