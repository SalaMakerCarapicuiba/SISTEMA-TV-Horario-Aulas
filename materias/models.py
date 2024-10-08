from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField

from horarios.models import Horario

class Materia(models.Model):
    DIAS_DA_SEMANA = [
        (2, 'Segunda-feira'),
        (3, 'Terça-feira'),
        (4, 'Quarta-feira'),
        (5, 'Quinta-feira'),
        (6, 'Sexta-feira'),
        (7, 'Sábado'),
    ]
    
    nome = models.CharField(max_length=100)
    horario = models.ManyToManyField(Horario, blank=True)  # Permitir nulo
    semestre = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    dias_da_semana = MultiSelectField(choices=DIAS_DA_SEMANA, max_length=100) 

    def __str__(self):
        return self.nome
