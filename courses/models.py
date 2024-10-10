from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps  # Para fazer o import tardio
from professors.models import Professor

class Course(models.Model):
    nome = models.CharField(max_length=150)
    turmas = models.ManyToManyField('turmas.Turma', blank=True)  # Usando string para atrasar a importação
    materias = models.ManyToManyField('materias_modelo.Materia', blank=True)  # Usando string para evitar circularidade
    professor_coordenador = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome
