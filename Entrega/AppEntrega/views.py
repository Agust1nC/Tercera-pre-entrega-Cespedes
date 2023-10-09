from django.shortcuts import render
from AppEntrega.models import Curso
from AppEntrega.forms import CursoFormulario

def inicio(request):
    return render(request, "AppEntrega/index.html")

def estudiantes(request):
    return render(request, "AppEntrega/estudiantes.html")

def profesores(request):
    return render(request, "AppEntrega/profesores.html")

def pnodocente(request):
    return render(request, "AppEntrega/personalnodocente.html")

def cursoFormulario(request):
    if request.method == 'POST':
        
            curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
            
            curso.save()
            
            return render(request, "AppEntrega/index.html")
        
    return render(request, "AppEntrega/cursoFormulario.html")

def apiCursoFormulario(request):
 
    if request.method == "POST":
 
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                curso.save()
                return render(request, "AppEntrega/index.html")
    else:
            miFormulario = CursoFormulario()
 
    return render(request, "AppEntrega/apiCursoFormulario.html", {"miFormulario": miFormulario})

def busqueda(request):

    if request.method == "POST":

        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():
            curso = miFormulario.save()
            return render(request, "AppEntrega/index.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "AppEntrega/busqueda.html", {"miFormulario": miFormulario})