from django import forms
from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
   # priority=forms.IntegerField(label ="Priority" ,min_value=1, max_value=10)

tasks= [ ]       #empty variable to store user entered data

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = [ ]
    return render(request,"tasks/index.html " , {
        "tasks":request.session["tasks"]
    })
#def add(request):
#return render(request ,"tasks/add.html")

def add(request):
    if request.method == "POST" :
        form = NewTaskForm(request.POST) #taking all the data from the user and filling it in from variable
        if form.is_valid():
            task = form.cleaned_data["task"]   # give all data user has submitted
            request.session["tasks"] += [task]
            tasks.append(task) #.reverse("tasks:index")
            return HttpResponseRedirect(reverse("tasks:index")) # redirects  the user to index page after entering data
        else:
            return render(request, "tasks/add.html", {
                "form":form             # will also show data that user has entered
                })      
    return render(request ,"tasks/add.html", {
        "form":NewTaskForm()             
    })
