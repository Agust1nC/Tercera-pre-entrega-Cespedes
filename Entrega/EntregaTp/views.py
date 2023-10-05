from django.http import HttpResponse
from django.template import Template, Context


def fprueba(request):
    return HttpResponse("FUNCION DE PRUEBA")


def test_template(request):
    
    # Abrimos el archivo HTML
    mi_html = open('./templates/index.html')
    
    # Cerramos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())
    
    # Cerramos el archivo previamente abierto, ya que esta cargado en la variable plantilla
    mi_html.close()
    
    # Creamos un contexto
    mi_contexto = Context()
    
    # Terminamos de construir el template renderizandolo con su contexto
    documento = plantilla.render(mi_contexto)
    
    return HttpResponse(documento)
    