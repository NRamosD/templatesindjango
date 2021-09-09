
from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, "./hello/index.html")

def gabi(request):
    return HttpResponse("Hello Gabi!")

def greets(request,name):
    return HttpResponse(f"Hello {name.capitalize()}!")