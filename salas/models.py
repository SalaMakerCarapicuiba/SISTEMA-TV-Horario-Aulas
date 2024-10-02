from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from materias.models import Materia

class Sala(models.Model):
    numero = models.IntegerField(validators=[MinValueValidator(0)])
    materias = models.ManyToManyField(Materia, blank=True)  # Relacionamento ManyToMany com blank=True
    
    
    