from django.db import models
from django.core.exceptions import ValidationError

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(default="")
    ra = models.CharField(max_length=20, unique=True, default="")
    max_horas = models.FloatField()
    horas_atuais = models.FloatField(default=0.0)

    def adicionar_horarios(self, horarios):
        """Adiciona horários ao professor, respeitando o limite máximo de horas."""
        print(horarios)
        horas_adicionais = horarios * 50 / 60  # Convertendo horários para horas
        if self.horas_atuais + horas_adicionais > self.max_horas:
            raise ValidationError("A soma das horas atuais com as novas horas excede o limite máximo.")
        self.horas_atuais += horas_adicionais
        self.save()
    
    def remover_horarios(self, horarios):
        """Remove horários do professor, garantindo que horas_atuais não fique negativa."""
        print(horarios)
        horas_removidas = horarios * 50 / 60  # Convertendo horários para horas
        if self.horas_atuais - horas_removidas < 0:
            raise ValidationError("Não é possível remover mais horas do que o total atual.")
        self.horas_atuais -= horas_removidas
        self.save()

    def __str__(self):
        return self.nome