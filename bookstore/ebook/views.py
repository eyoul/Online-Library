from django.shortcuts import render
from django.views.generic import View
from .models import Rbook
from .forms import RbookForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, "index.html", {})


# login and logout .
def logio(request):
    return render(request, "auth/logio.html", {})


# About Page .
def about(request):
    return render(request, "about.html", {})


# publisher add rbook page
def addRbook(request):
    print("request received")
    submitted = False
    if request.method == "POST":
        print("inside post")
        form = RbookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/rbook?submitted=True")
    else:
        form = RbookForm
        if "submitted" in request.GET:
            submitted = True
    return render(
        request, "publisher/add_rbook2.html", {"form": form, "submitted": submitted}
    )


def listBooks(request):
    books_list = Rbook.objects.all()
    print("rbooks: ", books_list)
    return render(request, "rbooks/rbooks.html", {"books_list": books_list})


class Book(View):
    context = {}

    def get(self, request):
        print("get handler")
        form = RbookForm()
        self.context["form"] = form
        return render(request, "publisher/add_rbook2.html", self.context)

    def post(self, request):
        print("post handler")
        print(request.FILES)
        form = RbookForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            print("form saved")
        else:
            print(form.errors)
        self.context["form"] = form
        return render(request, "publisher/add_rbook2.html", self.context)
