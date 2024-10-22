from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField

class Materia(models.Model):
    
    nome = models.CharField(max_length=100)
    semestre = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])

    def __str__(self):
        return self.nome
