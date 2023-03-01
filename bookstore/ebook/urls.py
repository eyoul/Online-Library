from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("logio", views.logio, name="logio"),
    path("about", views.about, name="about"),
    path("rbook", views.addRbook, name="addRbook"),
    path("list_books", views.listBooks, name="list_books"),
    path("rbook/<rbook_id>", views.show_rbook, name="show_rbook"),
    path("rbook/grade/<grade>", views.grade_rbooks, name="grade_rbooks"),
    path("dashboard/", views.home, name="home"),
    path("tbook", views.addTbook, name="addTbook"),
    path("list_tbooks", views.listTBooks, name="list_tbooks"),
    path("tbook/<tbook_id>", views.show_tbook, name="show_tbook"),
    path("tbook/grade/<grade>", views.grade_tbooks, name="grade_tbooks"),
]
