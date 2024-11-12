from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.apps import apps
from materias.models import Materia
from django.db.models.signals import post_save
from django.dispatch import receiver

class Turma(models.Model):
    PERIODO = [
        (1, 'Matutino'),
        (2, 'Vespertino'),
        (3, 'Noturno'),
    ]
    
    nome = models.CharField(max_length=150)
    semestre = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    periodo = models.IntegerField(choices=PERIODO)
    materias_copy = models.ManyToManyField(Materia, blank=True)
    curso = models.ForeignKey('courses.Course', on_delete=models.CASCADE)

    def _str_(self):
        return self.nome

    def delete(self, *args, **kwargs):
        # Remove todas as matérias copiadas antes de deletar a turma
        self.materias_copy.all().delete()
        super().delete(*args, **kwargs)


# Signal para criar matérias baseadas em modelo
@receiver(post_save, sender=Turma)
def criar_materias_baseadas_em_modelo(sender, instance, created, **kwargs):
    if created:
        # Obter todas as matérias do modelo associadas ao curso da turma
        materias_modelo_semestre = instance.curso.materias.filter(semestre=instance.semestre)

        # Criar novas matérias e associá-las à turma
        for materia_modelo in materias_modelo_semestre:
            nova_materia = Materia.objects.create(
                nome=materia_modelo.nome,
                semestre=materia_modelo.semestre,
                professor=None,
                horarios_por_dia={}
            )
            # Adicionar a nova matéria à relação Many-to-Many da turma
            instance.materias_copy.add(nova_materia)

        # Adicionar a turma ao curso
        instance.curso.turmas.add(instance)

# original
# from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.apps import apps  # Para acessar Curso via apps.get_model
# from materias.models import Materia
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# class Turma(models.Model):
#     PERIODO = [
#         (1, 'Matutino'),
#         (2, 'Vespertino'),
#         (3, 'Noturno'),
#     ]
    
#     nome = models.CharField(max_length=150)
#     semestre = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
#     periodo = models.IntegerField(choices=PERIODO)
#     materias_copy = models.ManyToManyField(Materia, blank=True)
#     curso = models.ForeignKey('courses.Course', on_delete=models.CASCADE)  # Usando string

#     def __str__(self):
#         return self.nome


# # Signal para criar matérias baseadas em modelo
# @receiver(post_save, sender=Turma)
# def criar_materias_baseadas_em_modelo(sender, instance, created, **kwargs):
#     if created:
#         # Obter todas as matérias do modelo associadas ao curso da turma
#         materias_modelo_semestre = instance.curso.materias.filter(semestre=instance.semestre)

#         # Criar novas matérias e associá-las à turma
#         for materia_modelo in materias_modelo_semestre:
#             nova_materia = Materia.objects.create(
#                 nome=materia_modelo.nome,
#                 semestre=materia_modelo.semestre,
#                 professor=None,  # Deixando o professor como None (nulo)
#                 horarios_por_dia={}  # Horários vazios
#             )
#             # Adicionar a nova matéria à relação Many-to-Many da turma
#             instance.materias_copy.add(nova_materia)

#         # Adicionar a turma ao curso
#         instance.curso.turmas.add(instance)  # Adiciona a turma ao campo 'turmas' do curso