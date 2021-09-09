from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("gabi",views.gabi, name="gabi"),
    path("<str:name>", views.greets, name="greets"),
    
]