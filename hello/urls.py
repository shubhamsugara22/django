from . import views
from django.urls import path
urlpatterns = [
    path("", views.index ,name="index" ) ,
    path("brian",views.brian, name="brian"),
    path("<str:name>" ,views.greet, name="greet"),
]