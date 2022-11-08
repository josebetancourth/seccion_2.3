from django.db import models

# Create your models here.

class profesor(models.Model):
    idprofesor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    carrera = models.CharField(max_length=20)
    
class materia(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    intensidad = models.CharField(max_length=20)
    
class curso(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    idprofe = models.ForeignKey(profesor,on_delete=models.CASCADE)
    idmateria = models.ForeignKey(materia,on_delete=models.CASCADE)

class estudiante(models.Model):
    idestudiante = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    curso1 = models.ForeignKey(curso,on_delete=models.CASCADE)
    
    