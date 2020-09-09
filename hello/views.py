from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world!")

def brian(request):
    return HttpResponse("hello")
def greet( request ,name):
    return HttpResponse(f"hello,{name}")