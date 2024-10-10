from django.db import models

from materias_modelo.models import Materia
from professors.models import Professor
from turmas.models import Turma

class Course(models.Model):
    nome = models.CharField(max_length=150)
    turmas = models.ManyToManyField(Turma, blank=True)
    materias = models.ManyToManyField(Materia, blank=True)
    professor_coordenador = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome
