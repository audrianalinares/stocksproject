from django.conf.urls import include, url
from django.contrib import admin
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about" ),
]