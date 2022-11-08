# Generated by Django 4.1 on 2022-11-05 19:42

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
                ('codmateria', models.IntegerField(primary_key=True, serialize=False)),
                ('nomateria', models.CharField(max_length=20)),
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
                ('codcurso', models.IntegerField(primary_key=True, serialize=False)),
                ('hora', models.CharField(max_length=20)),
                ('codmateria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.materia')),
                ('codprofe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='alumno',
            fields=[
                ('codalumno', models.IntegerField(primary_key=True, serialize=False)),
                ('nomalumno', models.CharField(max_length=20)),
                ('apealumno', models.CharField(max_length=20)),
                ('codcurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.curso')),
            ],
        ),
    ]
