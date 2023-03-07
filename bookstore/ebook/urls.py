from django.urls import path, include
from . import views


urlpatterns = [
    # home 
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("publisher/", views.home, name="home"),
    path("publisher/", views.home, name="home"),

#Reference book URLS

    path("publisher/rbook", views.addRbook, name="addRbook"),
    path("publisher/list_books", views.listBooks, name="list_books"),
    path("publisher/view/<rbook_id>", views.pdfview, name="pdfview"),
    path("publisher/update_rbook/<rbook_id>", views.update_rbook, name="update_rbook"),
    path("rbook/delete/<rbook_id>", views.delete_rbook, name="delete_rbook"),
    path("rbook/<rbook_id>", views.show_rbook, name="show_rbook"),
    path("rbook/grade/<grade>", views.grade_rbooks, name="grade_rbooks"),

# Text Book URLS

    path("publisher/tbook", views.addTbook, name="addTbook"),
    path("publisher/list_tbooks", views.listTBooks, name="list_tbooks"),
    path("publisher/update_tbook/<tbook_id>", views.update_tbook, name="update_tbook"),
    path("publisher/view1/<tbook_id>", views.pdfview1, name="pdfview1"),
    path("tbook/delete/<tbook_id>", views.delete_tbook, name="delete_tbook"),
    path("book", views.Book.as_view(), name="book"),

# Quiz  URLS

    path('quiz/quizhome', views.quizhome,name='quizhome'),
    path('quiz/addQuestion',  views.addQuestion,name='addQuestion'),
  
]
