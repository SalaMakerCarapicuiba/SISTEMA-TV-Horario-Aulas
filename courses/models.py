from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps  # Para fazer o import tardio
from professors.models import Professor
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete


class Course(models.Model):
    nome = models.CharField(max_length=150)
    turmas = models.ManyToManyField('turmas.Turma', blank=True)  # Usando string para atrasar a importação
    materias = models.ManyToManyField('materias_modelo.Materia', blank=True)  # Usando string para evitar circularidade
    professor_coordenador = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome

    @property
    def turma_count(self):
        return self.turmas.count()
    
@receiver(pre_delete, sender=Course)
def deletar_materias_modelo(sender, instance, **kwargs):
    # Deletar todas as matérias copiadas associadas à turma
    for materia in instance.materias.all():
        materia.delete()