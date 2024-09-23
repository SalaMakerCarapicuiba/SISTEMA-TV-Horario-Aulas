from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Turma(models.Model):
    PERIODO = [
        (1, 'Matutino'),
        (2, 'Vespertino'),
        (3, 'Noturno'),
    ]
    
    nome = models.CharField(max_length=150)
    semestre = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    periodo = models.IntegerField(choices=PERIODO)
   