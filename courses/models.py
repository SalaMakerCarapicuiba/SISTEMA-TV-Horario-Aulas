from django.db import models

from materias.models import Materia
from professors.models import Professor
from turmas.models import Turma

class Course(models.Model):
    nome = models.CharField(max_length=150)
    turmas = models.ManyToManyField(Turma)
    materias = models.ManyToManyField(Materia)
    professor_coordenador = models.ForeignKey(Professor, on_delete=models.CASCADE)
    

    
