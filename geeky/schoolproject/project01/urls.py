
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from project01  import views


urlpatterns = [
    path('', views.home),
    path('login', views.login),
    path('signup', views.signup),

    
]