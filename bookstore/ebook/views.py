from django.shortcuts import redirect, render
from django.views.generic import View
from .models import Rbook, Tbook
from .forms import *
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
    return render(request, "tbooks/subject_tbook.html", {"tbooks": tbooks})


def update_tbook(request, tbook_id):
    tbook = Tbook.objects.get(pk=tbook_id)
    if request.POST:
        form = TbookForm(request.POST, request.FILES, instance=tbook)
        if form.is_valid():
            form.save()
            return redirect("list_tbooks")
        else:
            print("invalid form: ", form.errors)
    else:
        form = TbookForm(None, instance=tbook)
    return render(request, "tbooks/update_tbook.html", {"tbook": tbook, "form": form})


def update_rbook(request, rbook_id):
    rbook = Rbook.objects.get(pk=rbook_id)
    if request.POST:
        form = RbookForm(request.POST, request.FILES, instance=rbook)
        if form.is_valid():
            form.save()
            return redirect("list_books")
        else:
            print("invalid form: ", form.errors)
    else:
        form = RbookForm(None, instance=rbook)
    return render(request, "rbooks/update_rbook.html", {"rboook": rbook, "form": form})

    return render(request, "publisher/subject_tbook.html", {"tbooks": tbooks})


# Create your views here.
def quizhome(request):
    if request.method == "POST":
        print(request.POST)
        counter = 0
        questions = Quiz.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            if "1" in str(request.POST.get(q.question)):
                submitted_answer = q.op1
            elif "2" in str(request.POST.get(q.question)):
                submitted_answer = q.op2
            elif "3" in str(request.POST.get(q.question)):
                submitted_answer = q.op3
            elif "4" in str(request.POST.get(q.question)):
                submitted_answer = q.op4
            print("submitted answer: ", submitted_answer)
            print("real answer: ", q.ans)
            print()
            if q.ans == submitted_answer:
                score += 10
                correct += 1
            else:
                wrong += 1

        percent = round(score / (total * 10) * 100, 2)
        context = {
            "score": score,
            "time": request.POST.get("timer"),
            "correct": correct,
            "wrong": wrong,
            "percent": percent,
            "total": total,
        }
        return render(request, "quiz/result.html", context)
    else:
        questions = Quiz.objects.all()
        context = {"questions": questions}
        return render(request, "quiz/quiz.html", context)


def addQuestion(request):
    if request.user.is_staff:
        form = addQuestionform()
        if request.method == "POST":
            form = addQuestionform(request.POST)
            if form.is_valid():
                form.save()
                return redirect("home")
        context = {"form": form}
        return render(request, "quiz/addQuestion.html", context)
    else:
        return redirect("quizhome")
