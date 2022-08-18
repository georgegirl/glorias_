from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_hello(request):
    return HttpResponse("This is the home page")

def run_page(request):
    return HttpResponse("ASSIGNMENT DEY TODAY")

def another_page(request):
    return HttpResponse("OTHER PAGINATION DEY")

def login_page(request):
    return render(request, "signup.html")
