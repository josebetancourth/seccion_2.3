from django.db import models

# Create your models here.

class profesor(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    titulo = models.CharField(max_length=20)
    
class materia(models.Model):
    codmateria = models.IntegerField(primary_key=True)
    nomateria = models.CharField(max_length=20)
    facultad = models.CharField(max_length=20)
    semestre = models.CharField(max_length=20)
    
class curso(models.Model):
    codcurso = models.IntegerField(primary_key=True)
    codprofe = models.ForeignKey(profesor,on_delete=models.CASCADE)
    codmateria = models.ForeignKey(materia,on_delete=models.CASCADE)
    hora = models.CharField(max_length=20)
    
class alumno(models.Model):
    codalumno = models.IntegerField(primary_key=True)
    nomalumno = models.CharField(max_length=20)
    apealumno = models.CharField(max_length=20)
    codcurso = models.ForeignKey(curso,on_delete=models.CASCADE)
   