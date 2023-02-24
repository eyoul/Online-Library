from django.urls import path, include
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   path('logio', views.logio, name='logio'),
   path('about', views.about, name='about'),
  
]
