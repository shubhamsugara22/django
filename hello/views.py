from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
    #return HttpResponse("hello world!")

def index(request):
    return render(request,"hello/index.html")
def brian(request):
    return HttpResponse("hello")

#def greet( request ,name):
    #return HttpResponse(f"hello,{name}")

def greet(request ,name):
    return render(request,"hello/greet.html" ,{
        "name": name.capitalize()
    })