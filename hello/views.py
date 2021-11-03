from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def jericho(request):
    return HttpResponse("Hello, Jericho!")

def mrRobot(request):
    return HttpResponse("Hello, my friend.")

def greet(request, name):
    return render(request, "hello/greet.html", {
        # context, want to provide to the template
        "name": name.capitalize()
    })