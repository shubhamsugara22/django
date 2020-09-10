from . import views
from django.urls import path
app_name="tasks"      # to uniquely identify apps having same file  to avoidnamespace collision
urlpatterns = [
    path("",views.index ,name="index"),
    path("add",views.add , name="add"),
]
