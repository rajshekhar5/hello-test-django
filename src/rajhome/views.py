from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return HttpResponse("<h1>hello</h1>")

def base_page(response):
    return render("templates/base.html")