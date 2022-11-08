# Generated by Django 4.1 on 2022-11-05 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='materia',
            fields=[
                ('codigomateria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombremateria', models.CharField(max_length=20)),
                ('facultad', models.CharField(max_length=20)),
                ('semestre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='profesor',
            fields=[
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='curso',
            fields=[
                ('codigocurso', models.IntegerField(primary_key=True, serialize=False)),
                ('hora', models.CharField(max_length=10)),
                ('cedprofesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.profesor')),
                ('codmateria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.materia')),
            ],
        ),
        migrations.CreateModel(
            name='alumno',
            fields=[
                ('codalumno', models.IntegerField(primary_key=True, serialize=False)),
                ('nombrealumno', models.CharField(max_length=20)),
                ('apellidalumno', models.CharField(max_length=20)),
                ('codcurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.curso')),
            ],
        ),
    ]
