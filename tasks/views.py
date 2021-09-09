from django import forms #para renderizar un form
from django.shortcuts import render
from django.http import HttpResponseRedirect #para redireccionar 
from django.urls import reverse #para seleccionar la redireccion mediante urls

#tasks = [] #si lo dejo aquí, todos los usuarios verán mi lista de tareas
# Create your views here.

class newTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

def index(request):
    if "tasks" not in request.session: #esto para implementar el concepto de sesiones
        request.session["tasks"] = []

    return render(request, "./tasks/index.html",{
        #"tasks": tasks     sin session
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = newTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            #forma 1:   
            #   tasks.append(task)
            #   return HttpResponseRedirect("./tasks")
            #forma 2:
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "./tasks/add.html", {
                "form": form
            })

    #este return es para que se muesren los campos que defini en el método 
    return render(request, "./tasks/add.html", {
        #la variable form se ubica en el add con doble corchete
        "form": newTaskForm()
    })