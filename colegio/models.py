from django.db import models

# Create your models here.

class materia(models.Model):
    idmateria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    intensidad = models.CharField(max_length=10)
    
class profesor(models.Model):
    idprofesor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    carrera = models.CharField(max_length=30)

class curso(models.Model):
    idcurso = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    codprofesor = models.ForeignKey(profesor,on_delete=models.CASCADE)
    codmateria = models.ForeignKey(materia,on_delete=models.CASCADE)
    
class estudiante(models.Model):
    idestudiante = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    celular = models.CharField(max_length=20)
    codcurso = models.ForeignKey(curso,on_delete=models.CASCADE)