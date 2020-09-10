from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    now=datetime.datetime.now()      #variable stores current date time 
    return render(request,"newyear/index.html",{
        "newyear":now.month==1 and now.date==1            #Change value to TRUE to check if it works
    })  # check condition if  month = 1 and date =1 it will pass it to newyear variable which     will render the output to condition in HTML page
