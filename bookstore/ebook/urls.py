from django.urls import path, include
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   # path('logio', views.logio, name='logio'),
   # path('about', views.about, name='about'),
   # path('student/gchat', views.gchat, name='gchat'),
   # path('publisher/tbook', views.tbook, name='tbook'),
   # path('publisher/rbook', views.rbook, name='rbook'),


   
]
