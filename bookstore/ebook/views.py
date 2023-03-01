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
            return HttpResponseRedirect("/rbook?submitted=True")
        else:
            print (form.errors)
            print(form.errors)
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
    
    
def home(request):
    return render(request, 'publisher/home.html', {})
def student(request):
    return render(request, 'student/home.html', {})


def home(request):
    return render(request, "dashboard/home.html", {})


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
            return HttpResponseRedirect("/tbook?submitted=True")
        else:
            print(form.errors)
    else:
        form = TbookForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, "add_textbook.html", {"form": form, "submitted": submitted})


def show_tbook(request, tbook_id):
    tbook = Tbook.objects.get(pk=tbook_id)
    return render(request, "tbooks/single_tbook.html", {"tbook": tbook})


def listTBooks(request):
    books_list = Tbook.objects.all()
    print("tbooks: ", books_list)
    return render(request, "tbooks/tbooks.html", {"books_list": books_list})


def show_rbook(request, rbook_id):
    rbook = Rbook.objects.get(pk=rbook_id)
    return render(request, "rbooks/single_rbook.html", {"rbook": rbook})


def grade_rbooks(request, grade):
    rbooks = Rbook.objects.filter(grade=grade)
    return render(request, "rbooks/subject_rbook.html", {"rbooks": rbooks})

def grade_tbooks(request, grade):
    tbooks = Tbook.objects.filter(grade=grade)
    return render(request, "tbooks/subject_tbook.html", {"tbooks": tbooks})