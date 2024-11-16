from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from professors.models import Professor


class Materia(models.Model):
    nome = models.CharField(max_length=100)
    semestre = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=True, null=True)

    
    # Campo JSON para armazenar os horários por dia da semana
    horarios_por_dia = models.JSONField(default=dict, blank=True, null=True)  # Ex: {"2": ["08:00-10:00"], "3": ["14:00-16:00"]}
    
    def __str__(self):
        return self.nome
