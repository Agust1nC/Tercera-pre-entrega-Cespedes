from django.db import models

class Estudiantes(models.Model):    
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()
    
    
    
class Profesores(models.Model):    
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()
    
    
    
class PersonalNoDocente(models.Model):    
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()    
    
    
    
class Curso(models.Model):
    nombre = models.CharField(max_length=25)    