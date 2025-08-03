from django.shortcuts import render
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", lambda request: render(request, 'main/home.html'), name='home'),
]