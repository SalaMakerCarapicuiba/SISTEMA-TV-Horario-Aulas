from django.db import models
from django.core.exceptions import ValidationError
from courses.models import Course  # Importa o model Course

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(default="")
    ra = models.CharField(max_length=20, unique=True, default="")
    max_horas = models.IntegerField()
    horas_atuais = models.IntegerField(default=0)
    cursos = models.ManyToManyField(Course, related_name='professores')  # Relacionamento ManyToMany

    def adicionar_horas(self, horas):
        """Adiciona horas ao professor, respeitando o limite máximo."""
        if self.horas_atuais + horas > self.max_horas:
            raise ValidationError("A soma das horas atuais com as novas horas excede o limite máximo.")
        self.horas_atuais += horas
        self.save()

    def __str__(self):
        return self.nome