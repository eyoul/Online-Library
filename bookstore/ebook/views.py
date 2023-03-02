from django.shortcuts import redirect, render
from django.views.generic import View
from .models import Rbook, Tbook
from .forms import RbookForm, TbookForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages

from . import views


def index(request):
    return render(request, "index.html", {})

# About Page .
def about(request):
    return render(request, "about.html", {})

def pdfview(request, rbook_id):
    rbook = Rbook.objects.get(pk=rbook_id)
    rbook.pdf = str(rbook.pdf).replace("ebook/static/", "")
    rbook.cover = str(rbook.cover).replace("ebook/static/", "")
    return render(request, "publisher/view.html", {"rbook": rbook})

def pdfview1(request, tbook_id):
    tbook = Tbook.objects.get(pk=tbook_id)
    tbook.pdf = str(tbook.pdf).replace("ebook/static/", "")
    tbook.cover = str(tbook.cover).replace("ebook/static/", "")
    return render(request, "publisher/view1.html", {"tbook": tbook})
    
# publisher add rbook page
def addRbook(request):
    print("request received")
    submitted = False
    if request.method == "POST":
        print("inside post")
        print("inside post new")
        form = RbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("rbook?submitted=True")
        else:
            print(form.errors)
            print(form.errors)
    else:
        form = RbookForm
        if "submitted" in request.GET:
            submitted = True
    return render(
        request, "publisher/add_rbook.html", {"form": form, "submitted": submitted}
    )


def listBooks(request):
    books_list = Rbook.objects.all()
    print("rbooks: ", books_list)
    for data in books_list:
        data.pdf = str(data.pdf).replace("ebook/static/", "")
        data.cover = str(data.cover).replace("ebook/static/", "")
    return render(request, "publisher/rbooks.html", {"books_list": books_list})


class Book(View):
    context = {}

    def get(self, request):
        print("get handler")
        form = RbookForm()
        self.context["form"] = form
        return render(request, "publisher/add_rbook.html", self.context)

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
        return render(request, "publisher/add_rbook.html", self.context)


def home(request):
    return render(request, "publisher/home.html", {})


def student(request):
    return render(request, "student/home.html", {})


def home(request):
    return render(request, "publisher/home.html", {})


# User is authenticated
def loginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_admin or user.is_superuser:
                return redirect("dashboard")
            elif user.is_librarian:
                return redirect("librarian")
            elif user.is_publisher:
                return redirect("publisher")
            else:
                return redirect("student")
        else:
            messages.info(request, "Invalid username or password")
            return redirect("home")


def addTbook(request):
    print("request received")
    submitted = False
    if request.method == "POST":
        print("inside tbook post")
        form = TbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("tbook?submitted=True")
        else:
            print(form.errors)
    else:
        form = TbookForm
        if "submitted" in request.GET:
            submitted = True
    return render(
        request, "publisher/add_tbooks.html", {"form": form, "submitted": submitted}
    )


def show_tbook(request, tbook_id):
    tbook = Tbook.objects.get(pk=tbook_id)
    return render(request, "publisher/single_tbook.html", {"tbook": tbook})



def listTBooks(request):
    list_tbooks = Tbook.objects.all()
    print("tbooks: ", list_tbooks)
    for data in list_tbooks:
        data.pdf = str(data.pdf).replace("ebook/static/", "")
        data.cover = str(data.cover).replace("ebook/static/", "")
    return render(request, "publisher/tbooks.html", {"list_tbooks": list_tbooks})


def show_rbook(request, rbook_id):
    rbook = Rbook.objects.get(pk=rbook_id)
    return render(request, "publisher/single_rbook.html", {"rbook": rbook})


def grade_rbooks(request, grade):
    rbooks = Rbook.objects.filter(grade=grade)
    return render(request, "publisher/subject_rbook.html", {"rbooks": rbooks})


def grade_tbooks(request, grade):
    tbooks = Tbook.objects.filter(grade=grade)
    return render(request, "publisher/subject_tbook.html", {"tbooks": tbooks})
