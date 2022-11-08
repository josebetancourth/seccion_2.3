from django.db import models

# Create your models here.

class profesor(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    titulo = models.CharField(max_length=20)

class materia(models.Model):
    codigomateria= models.IntegerField(primary_key=True)
    nombremateria = models.CharField(max_length=20)
    facultad = models.CharField(max_length=20)
    semestre = models.CharField(max_length=20)
    
class curso(models.Model):
    codigocurso = models.IntegerField(primary_key=True)
    cedprofesor = models.ForeignKey(profesor,on_delete=models.CASCADE)
    codmateria = models.ForeignKey(materia,on_delete=models.CASCADE)
    hora = models.CharField(max_length=10)

class alumno(models.Model):
    codalumno = models.IntegerField(primary_key=True)
    nombrealumno = models.CharField(max_length=20)
    apellidalumno = models.CharField(max_length=20)
    codcurso = models.ForeignKey(curso,on_delete=models.CASCADE)