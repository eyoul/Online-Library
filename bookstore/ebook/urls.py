from django.urls import path, include
from . import views


urlpatterns = [

    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("rbook", views.addRbook, name="addRbook"),
    path("list_books", views.listBooks, name="list_books"),
    path("book", views.Book.as_view(), name="book"),

   path('publisher/', views.home, name='home'),
   path('dashboard/', views.home, name='home'),

]
