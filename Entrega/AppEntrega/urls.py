from django.urls import path
from AppEntrega import views 

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('profesores/', views.profesores, name="Profesores"),
    path('personalnodocente/', views.pnodocente, name="PersonalNoDocente"),
    path('cursoform/', views.cursoFormulario, name="CursoForm"),
    path('apicursoform/', views.apiCursoFormulario, name="apiCursoForm"),
    path('busqueda/', views.busqueda, name="busqueda"),
]